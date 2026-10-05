"""Save a browser-authorized ScienceDirect PDF; never export login cookies.

Run with Python and pypdf. The temporary request JSON holds
the live URL, pii, and only the observed User-Agent/Referer headers. It is deleted
after this attempt. Browser navigation/authentication remains a separate step.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import urllib.parse
import urllib.request
from pypdf import PdfReader

def validate_pdf(path):
    data = path.read_bytes()
    if not data.startswith(b'%PDF-') or b'%%EOF' not in data[-2048:]:
        raise ValueError('Incomplete or non-PDF response')
    pdf = PdfReader(path)
    pages = len(pdf.pages)
    if pages < 1 or pdf.is_encrypted:
        raise ValueError('PDF structure could not be validated')
    return dict(pages=pages, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def download(request_file, route, library_dir):
  library_dir = Path(library_dir).resolve()
  library_dir.mkdir(parents=True, exist_ok=True)
  record = {'status': 'request_rejected', 'route': route}
  try:
    request = json.loads(request_file.read_text(encoding='utf-8'))
    pii = request['pii']
    assert re.fullmatch(r'S[0-9A-Z]{16}', pii), 'Invalid PII'
    url = urllib.parse.urlsplit(request['url'])
    role = request.get('role', 'main')
    assert role in ('main', 'article-with-SI', 'supplement')
    assert url.scheme == 'https' and not url.username and not url.password
    assert url.path.endswith('.pdf') and pii in url.path
    if url.hostname == 'pdf.sciencedirectassets.com':
        assert role == 'main'
        query = urllib.parse.parse_qs(url.query)
        issued = datetime.strptime(query['X-Amz-Date'][0], '%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc)
        assert (datetime.now(timezone.utc)-issued).total_seconds() < int(query['X-Amz-Expires'][0])-10, 'Reacquire an expired URL in the browser'
    else:
        assert url.hostname == 'ars.els-cdn.com' and role != 'main'
        assert re.fullmatch('/content/image/1-s2.0-'+pii+r'-mmc\d+\.pdf',url.path)
    headers = request['headers']
    assert set(headers) == {'User-Agent', 'Referer'}
    referer = urllib.parse.urlsplit(headers['Referer'])
    assert referer.scheme == 'https' and referer.hostname == 'www.sciencedirect.com'
    assert not referer.username and not referer.password
    assert all('\n' not in value and '\r' not in value for value in headers.values())
    output = library_dir/f'{pii}-{role}.pdf'
    assert not output.exists(), 'Existing original: deduplicate before downloading'
    part = output.with_suffix('.pdf.part')
    config = 'url = '+json.dumps(request['url'])+'\n'
    for name, value in headers.items():
        config += 'header = '+json.dumps(name+': '+value)+'\n'
    proxy = urllib.request.getproxies().get('https') if route == 'system-proxy' else None
    if proxy:
        config += 'proxy = '+json.dumps(proxy)+'\n'
    # Restart signed main PDFs; curl validates range support for attachments.
    resume_args = ['--continue-at','-','--retry','2','--retry-all-errors',
                   '--retry-delay','3'] if url.hostname == 'ars.els-cdn.com' else []
    route_args = ['--ipv4','--tls-max','1.2','--noproxy','*'] if route == 'direct' else []
    curl = shutil.which('curl.exe') or shutil.which('curl')
    if not curl:
        raise RuntimeError('curl is required')
    result = subprocess.run([curl,'--config','-',*route_args,*resume_args,'--silent','--fail',
        '--connect-timeout','30','--speed-limit','1','--speed-time','30',
        '--max-time','1800','--output',str(part),'--write-out','%{http_code}'],
        input=config, text=True, capture_output=True)
    article_url = urllib.parse.urlunsplit((referer.scheme, referer.netloc, referer.path, '', ''))
    http_status = result.stdout if re.fullmatch(r'\d{3}', result.stdout) else 'unknown'
    record = {'pii':pii, 'article_url':article_url, 'role':role, 'route':route,
              'curl_exit':result.returncode, 'http_status':http_status,
              'status':'transfer_failed'}
    if result.returncode:
        record['failure_kind'] = {6:'dns', 7:'connect', 22:'http_rejected',
            28:'timeout_or_stalled', 35:'tls_handshake', 60:'certificate_validation'}.get(
                result.returncode, 'transport_error')
        record['partial_bytes'] = part.stat().st_size if part.exists() else 0
        raise SystemExit(2)
    record['status'] = 'PDF_validation_failed'
    facts = validate_pdf(part)
    part.rename(output)
    record.update(status='pdf_structure_valid_identity_pending', file=str(output), **facts)
  except Exception:
    # Never expose a temporary URL, proxy credential, or parser diagnostic.
    record['failure_kind'] = 'request_or_dependency_error' if record['status'] == 'request_rejected' else 'pdf_validation_error'
    raise SystemExit(2) from None
  finally:
    request_file.unlink(missing_ok=True)
    log_dir = library_dir/'下载记录'
    log_dir.mkdir(exist_ok=True)
    log = log_dir/f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}-{record.get('pii','unidentified')}.json"
    log.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(record,ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--request', required=True, help='Temporary request JSON; deleted after the attempt')
    parser.add_argument('--library-dir', required=True, help='Explicit literature directory; never infer it from the installed skill path')
    parser.add_argument('--route', choices=('direct','system-proxy'), default='system-proxy')
    args = parser.parse_args()
    download(Path(args.request).resolve(), args.route, args.library_dir)

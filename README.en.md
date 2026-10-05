# robotics-research-writing

[中文](README.md) · [English](README.en.md) · [Distillation showcase / 真实文献蒸馏示例](examples/literature-distillation-showcase.md)

Extract **source-grounded, conditional, testable writing rules** from real robotics papers and author feedback, then apply them to contribution framing, argument structure, paragraph revision, and faithful Chinese-to-English translation.

This Codex skill focuses on writing decisions: how readers understand the engineering problem, how a mechanism produces the required effect, which evidence supports its value, and what each experiment establishes. Rules are stored together with their sources, applicable conditions, and counterexamples so later revisions remain traceable.

**Public scope: the workflow, empty state templates, an optional download helper, and one representative distillation showcase explicitly authorized for publication. The remaining distilled corpus, actual personal rule library, research profile, author materials, and validation logs stay private.**

The curated showcase is in the repository's `examples/` directory, outside the installable skill. The official installer installs only the framework and empty templates in `robotics-research-writing/`. Your personal state is initialized from the materials you actually provide.

## Purpose and workflow

Use it to:

- Study how papers frame problems and gaps, position contributions, and organize designs and evidence.
- Turn reading observations into personal rules with sources, transfer conditions, and counterexamples.
- Organize the strongest supported advantage and the shortest sufficient evidence chain from your methods, results, and figures.
- Audit defensive writing passage by passage while preserving scientific conditions needed for understanding.
- Translate Chinese into English faithfully, preserving facts, terminology, and claim strength.
- Revise rules from real feedback and record what changed and why.

The workflow is:

| Stage | Action | Output or check |
| --- | --- | --- |
| Materials | Verify identity, version, and accessible scope; convert PDF / Word to Markdown first | Source record, original files, and conversion |
| Understanding | Identify the problem, approach, main claims, and key evidence | Minimal understanding and reverse outline |
| Observations | Locate specific writing choices; separate source facts from interpretation | Page / section / paragraph / figure anchors |
| Conditional rules | Specify actions, applicability, counterexamples, and relationships to existing rules | Candidate rules or scope revisions |
| Application | Form a central claim from author facts before drafting prose | Revised text and fact / evidence checks |
| Validation | Check factual fidelity, structure, clarity, and fit to the task | Records of checks actually performed |
| Revision | Update only affected entries, retaining sources and reasons | Traceable personal rule versions |

A pattern in one paper can become a candidate observation; it does not automatically become a field standard. Research gaps require literature support. Writing templates do not create experiments, citations, measurements, or evidence of novelty.

### Three modes

| Mode | Typical request | Main deliverables |
| --- | --- | --- |
| A: Learn from literature | “Study this paper's writing” or “Distill 3 papers” | Paper understanding, reverse outline, source observations, conditional rules, and archive records |
| B: Apply to an author manuscript | “Restructure the results,” “Audit defensive writing,” or “Translate faithfully” | Draft or revised prose, necessary notes, and evidence gaps |
| C: Update and validate | “Incorporate this feedback” or “Test this rule” | Revisions to affected rules, reasons, and records of actual checks |

A download-only request produces archive results. A distillation-only request does not automatically revise an author manuscript. Local polishing does not restructure the whole paper. A simple text edit can be delivered directly without first building a complete knowledge base.

When no journal is specified, writing is organized for the research type and audience. Explanations default to Chinese; English-writing tasks produce English prose. Full parallel reading, file conversion, and statistical computation use appropriate tools when required.

## A real literature-distillation showcase

[Read the bilingual curated example](examples/literature-distillation-showcase.md): Ishida et al., *Exploration of fin stiffness for asymmetric thrust in a swimming robot*, RoboSoft 2024, [DOI](https://doi.org/10.1109/ROBOSOFT60065.2024.10522008).

The example shows how a real mechanism paper supports a reverse outline, three conditional candidate rules, checks of metrics and evidence, and explicitly labeled writing-transfer templates.

It is a curated paraphrase of an existing distillation record. Observations retained from that record are distinguished from examples newly constructed for this showcase. Candidate rules are not presented as independently validated conclusions. The example contains no PDF, full paper text, original figures, author manuscript, or percentage improvement in writing, and it is not automatically imported into your personal rule library.

## Installation

### Recommended: ask Codex to install it

Send this in Codex:

```text
Use skill-installer to install the skill in the robotics-research-writing
subdirectory of the Liuhy329/robotics-research-writing repository.
Use --repo Liuhy329/robotics-research-writing
and --path robotics-research-writing.
If a skill with the same name already exists, stop and do not overwrite my personal version.
```

Repository: [Liuhy329/robotics-research-writing](https://github.com/Liuhy329/robotics-research-writing). Install the subdirectory containing `SKILL.md`. After installation, explicitly invoke `$robotics-research-writing` on the next turn.

If using the provided `install-skill-from-github.py`, the corresponding arguments are:

```text
--repo Liuhy329/robotics-research-writing --path robotics-research-writing
```

The installer targets `$CODEX_HOME/skills/`, or `~/.codex/skills/` when `CODEX_HOME` is unset. It stops if a same-name destination directory already exists. Back up an existing personal version and compare its workflow and material locations before deciding how to migrate.

### Manual installation with Windows PowerShell

Git is required. These commands check both the destination and download directory first, and stop if either already exists.

```powershell
$skillRoot = if ([string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
    Join-Path $HOME '.codex\skills'
} else {
    Join-Path $env:CODEX_HOME 'skills'
}
$skillDir = Join-Path $skillRoot 'robotics-research-writing'
$repoDir = Join-Path (Get-Location) 'robotics-research-writing-public'
if (Test-Path -LiteralPath $skillDir) { throw "Destination exists; back up your personal version first: $skillDir" }
if (Test-Path -LiteralPath $repoDir) { throw "Download directory exists; use an empty directory: $repoDir" }
git clone https://github.com/Liuhy329/robotics-research-writing.git $repoDir
if ($LASTEXITCODE -ne 0) { throw 'Git download failed; the skill has not been copied.' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath (Join-Path $repoDir 'robotics-research-writing') -Destination $skillDir -Recurse
```

### Manual installation on Linux / macOS

Git is required. Existing destinations are left untouched. After a successful clone, only the installable subdirectory is copied.

```bash
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
skill_dir="$skill_root/robotics-research-writing"
repo_dir="$PWD/robotics-research-writing-public"
if [ -e "$skill_dir" ] || [ -e "$repo_dir" ]; then
  printf '%s\n' 'The skill or download directory already exists; back it up or use an empty directory.'
else
  git clone https://github.com/Liuhy329/robotics-research-writing.git "$repo_dir" &&
  mkdir -p "$skill_root" &&
  cp -R "$repo_dir/robotics-research-writing" "$skill_dir"
fi
```

## Five-minute quick start

1. Open your research project workspace and prepare one paper or a passage to revise.
2. Specify the mode, paper count or section, desired deliverable, and authorized research directory for saved materials.
3. Explicitly invoke `$robotics-research-writing`; convert PDF / Word to Markdown before reading.
4. Review the actual reading scope, evidence anchors, and generated file locations before deciding to apply a rule.

For a first literature-learning task, send:

```text
$robotics-research-writing
Distill the paper I provide, focusing on how design is connected to experimental argument.
Learn from the literature only; do not revise an author manuscript.
Convert to Markdown first, then read and inspect the key figures and tables.
Save personal records to .robotics-writing/ in the current research project.
Without author materials, use explicitly labeled structural placeholders for transfer examples.
Deliver the actual reading scope, reverse outline, conditional candidate rules, and saved file locations.
```

### Input checklist

Provide the materials you actually have; a complete profile is not required on first use:

| Input | What it helps determine |
| --- | --- |
| PDF, Word, accessible HTML, DOI, or supplied paper text | Sources that can actually be read and verified |
| Research direction and type, target audience / journal | Which observations and rules apply |
| One paper or an explicit batch count and selection direction | Task scope and stopping point |
| Author draft, methods, results, figures, and citations | Real facts and evidence available for revision |
| Revision depth, language, terminology list, and preservation requirements | Delivery format and editing boundaries |
| Research directory and existing literature-management approach | Where personal records and files are stored |

When an input is missing, explain which step it affects and complete the work that remains possible. Abstract-only access is recorded as such. Full-paper distillation is not inferred from a title or abstract.

### Expected outputs

| Task | Deliverables to expect |
| --- | --- |
| Literature learning | Identity and reading scope, minimal understanding, reverse outline, anchored observations, and candidate rules with their relationships |
| Author writing | Readable prose / revision, with adjustment notes and unresolved gaps outside the manuscript text |
| Defensive-writing audit | Original passage, issue type, information to retain, revision, and whether scientific meaning changes |
| Rule update | Actual revised entries, sources, reasons, coverage changes, and validation performed |

Tasks that save materials also report output paths and actual completion state. If file writing is unavailable, provide content that can be saved and state that it has not yet been written.

## Personal materials and state

The installed public `references/` directory retains empty templates and methods. Actual knowledge is saved on demand in `.robotics-writing/` within **your research project workspace**:

```text
your-research-project/
└── .robotics-writing/
    ├── profile-state.md     # Research needs, coverage, and current state
    ├── writing-rules.md     # Actual personal rules, sources, and applicability
    ├── source-index.md      # Actual source index, versions, and material paths
    ├── validation.md        # Actual checks, validation, and revision records
    ├── distillations/       # Individual paper-learning records
    ├── literature/          # Original papers, or links to an existing library
    └── processed/           # Markdown conversions and cleaned materials
```

Required state files are initialized from templates as needed; every directory need not be created at once. Existing literature libraries can be reused by registering their paths. Original files are not automatically moved, and stable source IDs are not reassigned.

Files use verified official titles, with incompatible filename characters normalized and necessary version or supplement suffixes. Compare hashes and versions before handling a name collision. Use your existing categories; without a taxonomy, store by title and express finer distinctions with tags.

This repository ignores `.robotics-writing/`. If using the skill in another Git project, add the following to **that project's** `.gitignore`:

```gitignore
.robotics-writing/
```

If original papers are stored outside this directory, manage their sharing scope separately in the relevant project. `.gitignore` does not untrack files already committed.

### Source-record schema

See [source-index.md](robotics-research-writing/references/source-index.md) for the complete schema. Main field groups are:

| Field group | Contents |
| --- | --- |
| Identity | Stable ID, official title, authors, year, venue, DOI / stable source page; mark unverified fields |
| Version and role | Published version / preprint / revision; main article / article with supplement / separate supplement; related versions |
| Files | Original and Markdown paths, page count, byte count, and SHA-256 |
| Acquisition | Query and selection conditions, inspected scope, selection rationale, time, and normal access route |
| Reading | Actual sections, pages, and figures inspected; conversion gaps and full-text / abstract / excerpt limits |
| Distillation | Record location, rule support / revision, counterexamples / conflicts, or reason for no new information |

Temporary signed download URLs, cookies, account tokens, and credentials do not enter the source index.

### Conditional-rule schema

See [writing-rules.md](robotics-research-writing/references/writing-rules.md) for the complete schema. A usable rule records:

| Field | Requirement |
| --- | --- |
| Stable ID, name, and state | Identify the decision being changed; use a state supported by actual evidence |
| Action | What writing choice to make under which conditions |
| Applicable / inapplicable conditions | Research type, audience, section purpose, evidence needs, and counterexamples |
| Observable facts | Source ID, anchors, short quotation, or faithful paraphrase |
| Interpretation and rationale | The writing choice's argumentative role, separate from source facts |
| Evidence scope | Actual reading scope, study independence, supporting examples, and counterexamples |
| Transfer example | Authorized author facts, or clearly labeled placeholders / constructed examples |
| Validation and changes | Validation record, actual result, date, prior state, changes, and reasons |

Compare a candidate with existing rules as new, supporting, scope-revising, counterexample, conflicting, duplicate, or not adopted. When it adds nothing new, record the paper as read or add an example rather than another equivalent rule. Personal rule IDs do not appear in manuscript prose.

## Six prompts you can copy

### 1. Distill one paper

```text
$robotics-research-writing
Study the robotics paper I provide and distill its writing methods only; do not revise my draft.
Convert PDF / Word to Markdown first, retaining originals and page, section, paragraph, and figure anchors.
Report the actual reading scope, then map problem–claim–evidence and build a reverse outline.
Extract observations that add information, with sources, roles, transfer conditions, and counterexamples.
Save to the current research project's .robotics-writing/; without author materials, use labeled placeholders.
```

### 2. Learn from a batch with a fixed direction and count

```text
$robotics-research-writing
This request authorizes 3 robotics mechanism-design papers, focusing on
“engineering problem → how structure produces motion → how experiments establish design value.”
Check the source index and deduplicate first; prefer my local files, then use lawful access if needed.
Verify identity, convert, read, save, and check each paper; stop after 3 papers.
Distill only; do not edit an author manuscript or create a scheduled task.
If fewer than 3 can be completed, report the actual count and missing inputs without claiming completion.
```

Replace the count and direction with your actual authorization. Link preprints, published versions, and supplements from the same study. Report file counts, paper-version counts, and independent-study counts separately.

### 3. Organize the manuscript's central argument

```text
$robotics-research-writing
Restructure the introduction and results using the draft, results, and figures below.
First state the central claim, strongest confirmed advantage, and supporting evidence chain; then revise.
Organize as “problem → gap → idea → strongest confirmed result.”
Order results by argumentative purpose, not experiment chronology. Gaps need source support.
Preserve numbers, conditions, citations, and result meaning; list missing inputs separately.
Keep manuscript text separate from revision notes.
```

### 4. Audit defensive writing passage by passage

```text
$robotics-research-writing
Audit the text below and provide for each relevant passage:
original → issue type → information to retain → revision → whether scientific meaning changes.
Organize around demonstrated advantages without summarizing weaknesses on the reviewer's behalf.
Retain real uncertainty, comparison conditions, and test scope where they affect understanding.
Do not turn observation into mechanism validation, or the highest tested point into a global optimum.
```

### 5. Translate faithfully from Chinese to English

```text
$robotics-research-writing
Translate the manuscript passage below into natural, accurate academic English.
Prioritize fidelity, then natural expression; preserve numbers, units, terms, equations, citations, and claim strength.
Do not broaden applicability or report unmeasured performance as a result.
Deliver English prose; explain terminology ambiguities and meaning-affecting gaps separately.
```

### 6. Update rules from real feedback

```text
$robotics-research-writing
Below are the original passage, revision, and my specific feedback.
Check existing rules and classify this as new, supporting, scope-revising, counterexample, conflicting, or a one-off edit.
Update only affected entries; retain IDs, sources, prior states, changes, and reasons.
Save records to .robotics-writing/; do not modify other skills or global memory.
When testing, distinguish real author materials from constructed cases and report the actual scope checked.
```

## Scientific evidence and fair comparisons

Build the narrative around the strongest demonstrable advantage. Explain why it matters and which results support it. Each experiment should have an argumentative purpose. Abstracts and introductions state the problem, gap, idea, and key result; conclusions reinforce what has been demonstrated.

Evaluation dimensions should serve the research goal, and comparison conditions must be stated. Differences in goals and reasonable trade-offs can explain results; advantages cannot be manufactured by dropping reported outcomes, changing denominators, or concealing conditions.

For robotics writing, check:

- Simulation / hardware, fixed-position force tests / free motion, and single demonstrations / repeated trials.
- Frames / cycles / trials / independent prototypes; best / representative / mean values.
- Open-loop / closed-loop, preprogrammed execution / autonomous decisions, and external power or computation / self-contained operation.
- One environment / generalization, component / system, observation / mechanism validation, and statistical significance / engineering relevance.
- Definitions, units, denominators, and statistical units for speed, load, energy, efficiency, accuracy, adhesion force, and success rate.
- Size, mass, power supply, payload, environment, task, control settings, and aggregation methods.

Physical-quantity names must match calculations; for example, a force–time integral is not mechanical work. A literature table with different conditions is not a controlled superiority experiment. The highest tested point is not a global optimum. Literature results, unmeasured variables, and repetition counts from adjacent experiments are not imported into the author's results.

## Dependencies and optional tools

Codex handles the core reading and writing workflow; no Python package is mandatory. Check currently installed capabilities, then choose the smallest useful tool set for the task.

| Scenario | Optional tools and purpose |
| --- | --- |
| PDF / Word to Markdown | `markitdown` or local extractors; inspect original pages when conversion is unreliable |
| Full-paper close reading / parallel translation | `nature-reader`, following the user's actual requested scope |
| Citation verification | `nature-ref-verifier` or original papers and author / publisher pages |
| ScienceDirect page access | A currently available browser skill, optionally with `sd-search` / `sd-download` |
| Specific journal style | `nature-writing` / `nature-polishing` when requested |
| Statistical reporting / defensive phrasing | `nature-statistics` / `anti-defensive-writing`; statistical reporting does not replace raw-data analysis |
| Local PDF download helper | Python 3.9+, `pypdf`, and `curl.exe` or `curl` |

Optional companion skills are not installed by this repository. Listing a tool does not guarantee its availability in your environment. If a conversion skill is missing, local extraction can produce anchored Markdown; retain source images and record content that cannot be recovered.

### Optional ScienceDirect download workflow

You need existing lawful institutional, subscription, or open-access permission. Sign in normally in the browser; Codex follows the actual page to obtain a PDF URL. The included helper handles local transfer and structural validation, not login or access rights.

From the repository root, install the optional dependency and inspect arguments:

```powershell
py -3 -m pip install -r requirements.txt
py -3 robotics-research-writing/scripts/sciencedirect_download.py --help
```

On Linux / macOS, replace `py -3` with `python3`. In an installed skill, the helper is under `scripts/`; install `pypdf` only when needed.

Codex creates a dedicated temporary request JSON from an actual browser request. Do not manually export cookies. An explicit personal literature directory is required:

```text
python scripts/sciencedirect_download.py --request /path/to/temporary-request.json --library-dir /path/to/research/.robotics-writing/literature --route system-proxy
```

Run this from the skill directory, replacing paths with the actual task locations. The optional `direct` route only controls the current transfer; it does not change access authorization. Authentication, verification challenges, and permission refusals must be resolved through normal access.

The helper first writes `.pdf.part`. It renames the file to `.pdf` after checks of structure, page count, encryption state, and SHA-256 recording. `pdf_structure_valid_identity_pending` still requires title / DOI verification. Opening a reader, triggering a download, and saving a local file are distinct states. The dedicated request file is removed at the end of that attempt; signed URLs and download logs stay out of public output.

See [sciencedirect-acquisition.md](robotics-research-writing/references/sciencedirect-acquisition.md) for the full workflow, bounded recovery, and status definitions.

## Troubleshooting and validation scope

| Situation | Response |
| --- | --- |
| Rule templates are empty after installation | This is the initial public framework; build records from real inputs in the project's `.robotics-writing/` |
| A same-name personal skill already exists | The installer stops; back up and compare versions before changing existing rules or sources |
| The skill is not discovered on the next turn | Check that the install directory contains `SKILL.md` and the correct name, then invoke explicitly; file presence is not proof of loading |
| PDF is partial, returns HTML, or remains `.part` | Do not count it as acquired; retain the checkpoint, attempt bounded recovery, and validate again |
| Signed URL expired or institutional login lapsed | Return to the normal article entry point for a fresh link; the user completes login verification, without unlimited retries |
| Browser or conversion skills are unavailable | Work on existing local materials first; identify the tool needed for the missing stage without claiming download or full reading |
| Columns, equations, or tables convert incorrectly | Keep the original conversion, inspect source pages, and repair anchors; mark unrecoverable content and retain source images |
| Only an abstract / excerpt is available, or key figures are missing | Analyze the actual scope and list conclusions affected by gaps; do not record full-paper completion |
| Papers support conflicting rules | Check research type, section purpose, and evidence; retain counterexamples and narrow scope or reduce priority as needed |

The [validation workflow](robotics-research-writing/references/validation.md) distinguishes format checks, constructed cases, and real writing transfer. Prefer real materials not used to derive the rule, hold facts and tasks fixed, and assess factual fidelity, claim–evidence alignment, structure, clarity, terminology, and task fit.

Vocabulary difficulty, length, or “looking like a top-journal paper” are not effectiveness tests. A case used to tune a rule is no longer independent validation. Installation, format checks, and offline helper checks do not establish writing effectiveness or successful live institutional downloads.

## Public files and sharing boundaries

```text
README.md / README.en.md                  # Bilingual usage documentation
examples/literature-distillation-showcase.md # The single authorized curated showcase
robotics-research-writing/
├── SKILL.md
├── agents/openai.yaml
├── references/                          # Empty state templates and generic workflows
└── scripts/sciencedirect_download.py
requirements.txt / .gitignore / .gitattributes
```

Other original papers, supplements, extracted full text, distillation records, actual source indexes, personal rules, research profiles, author manuscripts, experiment data, and feedback logs remain in personal projects. Permission to publish the curated showcase does not extend to those materials.

Personal outputs are not automatically committed or pushed and are not written back into public templates. Review staged files before publishing. API keys, login credentials, cookies, and signed download URLs stay out of the repository. Processing private materials through external services requires appropriate authorization; original files are preserved.

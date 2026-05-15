# OpenAI Codex / Copilot Setup for Complete Beginners

This guide explains how to get **Spine Harmony** running with OpenAI's coding-agent workflow, usually called **Codex**. Some people may describe this as using an AI "copilot" for files and notes. The practical setup is the same: give the coding agent the Spine Harmony instructions, keep your real medical data in a separate private workspace, and ask the agent to organize notes, symptom logs, and clinician questions.

> **Important naming note:** GitHub Copilot is a Microsoft/GitHub product. OpenAI's coding-agent product is commonly called **Codex**. This guide uses **OpenAI Codex / Copilot-style workflow** to cover the common beginner wording, but the actual commands below use OpenAI Codex.

> **Medical and privacy warning:** Spine Harmony is not medical advice, diagnosis, treatment guidance, emergency triage, radiology interpretation, or a medical device. If you paste or upload medical records into Codex, ChatGPT, a cloud IDE, or another hosted AI tool, you may be disclosing medical information to that provider. Review the provider's terms, privacy policy, retention settings, and your own comfort level before adding real records.

## What you will set up

You will create two folders:

```text
Documents/
├── spine-harmony-agent/          # public template repo; no private medical files
└── spine-harmony-private/        # your private workspace; do not upload to GitHub
```

Codex should work inside `spine-harmony-private/`. The public repo is only the instruction and template pack.

## Plain-English overview

Spine Harmony works because an AI coding agent can read project instructions and workspace files:

1. `AGENTS.md` tells the agent how a Spine Harmony assistant should behave.
2. `templates/` contains blank starter files for your profile, journal, symptom tracker, Q&A log, and handoff notes.
3. Your private folder stores your real notes and records.
4. Codex helps organize and summarize your files, but it must not make medical decisions.

## Before you begin

You need:

- A computer where you can install apps and use a terminal.
- An OpenAI account with access to Codex or the OpenAI Codex CLI.
- Git, or the ability to download a ZIP file from GitHub.
- Basic comfort copying and pasting commands.

Optional but helpful:

- Visual Studio Code or another text editor.
- A dedicated folder such as `Documents/SpineHarmony/` for all local files.

## Step 1 — Get the Spine Harmony files

### Option A: beginner-friendly download from GitHub

1. Open the Spine Harmony GitHub repository in your browser.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Unzip it.
5. Rename the unzipped folder to `spine-harmony-agent`.
6. Move it into your `Documents` folder.

### Option B: terminal clone

Open Terminal or PowerShell and run:

```bash
cd ~/Documents
git clone https://github.com/d2ma-tech/spine-harmony-agent.git
```

If `git` is not installed, use Option A or install Git first.

## Step 2 — Create your private workspace

Create a separate folder for your real data:

```bash
cd ~/Documents
mkdir spine-harmony-private
```

This folder is intentionally separate from the public GitHub repo. Do **not** push this private folder to GitHub.

## Step 3 — Make the private folder a local git workspace

The Codex CLI expects to work inside a git repository. Your private folder can be a local-only git repo that is never pushed anywhere.

```bash
cd ~/Documents/spine-harmony-private
git init
```

This is only for local file tracking. It does not upload anything by itself.

## Step 4 — Add a privacy-first `.gitignore`

Inside `spine-harmony-private`, create a `.gitignore` file so common private or bulky medical files are not accidentally committed.

On macOS/Linux:

```bash
cat > .gitignore <<'EOF'
# Real medical/private data — keep out of git history
records/
imaging/
exports/
reports/private/
consultations/
transcripts/
*.pdf
*.doc
*.docx
*.zip
*.7z
*.tar
*.gz
*.dcm
*.dicom
*.nii
*.mha
*.mhd
*.nrrd

# Secrets and local environment files
.env
*.key
*.pem
*token*
*secret*

# Operating-system/editor clutter
.DS_Store
Thumbs.db
.vscode/
.idea/
EOF
```

On Windows PowerShell:

```powershell
@'
# Real medical/private data — keep out of git history
records/
imaging/
exports/
reports/private/
consultations/
transcripts/
*.pdf
*.doc
*.docx
*.zip
*.7z
*.tar
*.gz
*.dcm
*.dicom
*.nii
*.mha
*.mhd
*.nrrd

# Secrets and local environment files
.env
*.key
*.pem
*token*
*secret*

# Operating-system/editor clutter
.DS_Store
Thumbs.db
.vscode/
.idea/
'@ | Set-Content .gitignore
```

## Step 5 — Copy the Spine Harmony instructions

From your `Documents` folder, copy the public instruction file into your private workspace:

```bash
cd ~/Documents
cp spine-harmony-agent/AGENTS.md spine-harmony-private/AGENTS.md
```

Why this matters: Codex and other coding agents can read `AGENTS.md` as project instructions. This tells the agent to stay spine-specific, preserve privacy, avoid diagnosis/treatment advice, and keep real patient data out of public outputs.

## Step 6 — Copy the starter templates

Run:

```bash
cd ~/Documents
cp spine-harmony-agent/templates/USER.md spine-harmony-private/USER.md
cp spine-harmony-agent/templates/SpineHarmony_Journal.md spine-harmony-private/SpineHarmony_Journal.md
cp spine-harmony-agent/templates/qa-log.md spine-harmony-private/qa-log.md
cp spine-harmony-agent/templates/symptom-tracker.md spine-harmony-private/symptom-tracker.md
cp spine-harmony-agent/templates/handoff.md spine-harmony-private/handoff.md
```

You now have a private workspace with the minimum starter files.

## Step 7 — Add private folders for your own records

Create folders for files you may want to organize locally:

```bash
cd ~/Documents/spine-harmony-private
mkdir -p records imaging exports reports/private consultations transcripts
```

Keep real records in these folders. They are ignored by the `.gitignore` above.

## Step 8 — Fill in the starter files by hand first

Open `spine-harmony-private` in a text editor and edit:

- `USER.md` — basic profile and preferences;
- `SpineHarmony_Journal.md` — your spine-health timeline;
- `symptom-tracker.md` — current symptom and pain tracking;
- `qa-log.md` — questions and answers you want preserved;
- `handoff.md` — a short summary for future sessions.

Use plain language. You do not need perfect medical formatting.

Example safe first entries:

```markdown
# USER

- Name: [your name or initials]
- Location/timezone: [your timezone]
- Spine condition summary: [brief plain-English summary]
- Current clinicians: [optional]
- Privacy preference: Keep real medical files out of public repos.
```

```markdown
# Spine Harmony Journal

## Current spine-health summary

- Main issue: [plain-English description]
- Key imaging/report facts: [source facts only]
- Current treatment plan from clinician: [what your clinician said]
- Open questions for next appointment: [list]
```

## Step 9 — Install OpenAI Codex CLI

If you already have OpenAI Codex available in your coding environment, skip to Step 10.

If you are using the Codex CLI, install it with npm:

```bash
npm install -g @openai/codex
```

Then confirm it runs:

```bash
codex --version
```

If the command is not found, check that Node.js/npm are installed and that your terminal can see globally installed npm packages.

## Step 10 — Sign in to OpenAI / Codex

Follow the login or authentication instructions shown by your Codex environment. Depending on your setup, this may be:

- browser-based login;
- an OpenAI API key stored in your shell environment;
- an authenticated Codex CLI session;
- a hosted OpenAI coding-agent workspace.

Do **not** put API keys, tokens, passwords, or recovery codes inside your Spine Harmony files.

## Step 11 — Start Codex inside the private workspace

Run Codex from the private folder, not the public template repo:

```bash
cd ~/Documents/spine-harmony-private
codex
```

Or for a one-shot instruction:

```bash
cd ~/Documents/spine-harmony-private
codex exec "Read AGENTS.md, USER.md, SpineHarmony_Journal.md, symptom-tracker.md, qa-log.md, and handoff.md. Summarize what is currently known, list missing information, and suggest clinician-verification questions. Do not diagnose or recommend treatment."
```

If your Codex environment has a graphical interface, open the folder `spine-harmony-private` as the project/workspace and make sure it can see `AGENTS.md`.

## Step 12 — First safe prompt

Paste this as your first prompt:

```text
Read AGENTS.md and follow it as the project instruction.

Then read USER.md, SpineHarmony_Journal.md, symptom-tracker.md, qa-log.md, and handoff.md.

Please give me:
1. a concise spine-history summary grounded only in the files;
2. missing information I should add;
3. questions to ask my clinician;
4. any red-flag symptoms that should be handled by urgent medical care, without trying to triage severity.

Do not diagnose, recommend treatment, interpret imaging as a clinician, or tell me to start/stop/change medication, exercise, procedures, or surgery.
```

## Step 13 — Commit only the safe starter files locally

After you have created the initial workspace, you may make a local commit so you can track your own edits over time:

```bash
cd ~/Documents/spine-harmony-private
git status
git add AGENTS.md USER.md SpineHarmony_Journal.md qa-log.md symptom-tracker.md handoff.md .gitignore
git commit -m "Initialize private Spine Harmony workspace"
```

Do not add raw medical records, imaging, PDFs, transcripts, or private generated reports to git.

## Step 14 — Daily or weekly use

Use Codex to help maintain your files, for example:

```text
Read AGENTS.md and symptom-tracker.md. Add this new symptom note to the tracker while preserving my raw facts. Then update the trend summary cautiously without saying the treatment worked unless a clinician said that.

New note:
[Paste your note here]
```

```text
Read AGENTS.md, SpineHarmony_Journal.md, and qa-log.md. Prepare a short question list for my next spine appointment. Separate source facts from interpretation. Do not recommend treatment.
```

```text
Read AGENTS.md and handoff.md. Update handoff.md so another session can understand the current state, open questions, and safety boundaries. Keep it concise.
```

## Beginner safety checklist

Before adding real records, check:

- [ ] I am working in `spine-harmony-private`, not `spine-harmony-agent`.
- [ ] `AGENTS.md` exists in the private folder.
- [ ] `.gitignore` exists in the private folder.
- [ ] I understand that uploading/pasting medical data into hosted AI tools may disclose it to that provider.
- [ ] I will not push the private folder to GitHub.
- [ ] I will not ask the agent to diagnose me, choose treatment, change medication, or interpret imaging as a clinician.
- [ ] I will ask qualified clinicians to verify medically important conclusions.

## What to ask Codex to do

Good tasks:

- Organize your spine-health timeline.
- Turn rough symptom notes into structured diary entries.
- Create a clinician question list.
- Summarize a document you provide, with source caveats.
- Compare what two notes say and identify contradictions.
- Draft a patient-facing report for clinician review.
- Keep a handoff file updated for future sessions.

Avoid asking Codex to:

- diagnose the pain source;
- decide whether you need surgery;
- tell you to start, stop, or change medication;
- prescribe exercises or rehabilitation changes;
- interpret MRI/DICOM images as a radiologist;
- replace urgent care, emergency care, a physician, or a physical therapist.

## If you use ChatGPT instead of Codex CLI

If you are using a ChatGPT project, OpenAI web workspace, or other OpenAI copilot-style interface instead of the Codex CLI:

1. Create a project called `Spine Harmony`.
2. Add the contents of `AGENTS.md` as the project instruction.
3. Upload or paste only the files you are comfortable sharing with OpenAI.
4. Keep your private source folder locally as the source of truth.
5. Avoid uploading raw imaging, full medical records, or private reports unless you understand the privacy implications.
6. Ask ChatGPT to produce edits you can copy back into your local files.

This is less file-native than Codex, but the same safety rules apply.

## Troubleshooting

### Codex says it cannot see my files

Make sure you started Codex from the private folder:

```bash
cd ~/Documents/spine-harmony-private
pwd
ls
codex
```

You should see `AGENTS.md`, `USER.md`, `SpineHarmony_Journal.md`, `qa-log.md`, `symptom-tracker.md`, and `handoff.md`.

### Codex ignores the Spine Harmony rules

Tell it explicitly:

```text
Read AGENTS.md again and follow it as the project instruction. Stay within the Spine Harmony boundaries: organize, summarize, track, and prepare clinician questions; do not diagnose or recommend treatment.
```

### I accidentally put private files in the public repo folder

1. Move them out of `spine-harmony-agent` and into `spine-harmony-private`.
2. Do not commit them.
3. If they were already committed, do not push. Get help cleaning git history before sharing the repo.

### `git status` shows medical files ready to commit

Do not commit. Add the file type or folder to `.gitignore`, then check again:

```bash
git status
```

### Codex suggests medical advice

Push it back inside the boundary:

```text
Do not recommend treatment or make medical decisions. Reframe this as: source facts, uncertainty, questions for my clinician, and safety boundaries.
```

## Minimal no-terminal version

If you cannot use terminal commands:

1. Download the repo as a ZIP from GitHub.
2. Create a folder called `spine-harmony-private` somewhere safe on your computer.
3. Copy `AGENTS.md` from the repo into `spine-harmony-private`.
4. Copy the files from `templates/` into `spine-harmony-private`.
5. Open the private folder in your OpenAI/Codex/ChatGPT workspace if supported.
6. Paste the first safe prompt from Step 12.
7. Keep real medical files out of GitHub and public folders.

## Final reminder

Spine Harmony is a structured patient-side memory and preparation system. It can help you stay organized, track symptoms, and ask better questions. It should not diagnose, replace qualified clinicians, or make treatment decisions.

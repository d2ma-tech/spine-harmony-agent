# Claude Code / Claude Cowork Setup for Complete Beginners

This guide explains how to get **Spine Harmony** running in Claude Code or a Claude-based coding-agent workspace. Some users describe this as using Claude as a "coworker" or "cowork" setup; the practical steps are the same: give Claude the Spine Harmony instructions, keep your private medical files in a local private workspace, and use Claude to organize notes, drafts, and questions.

> **Medical and privacy warning:** Spine Harmony is not medical advice, diagnosis, treatment guidance, emergency triage, radiology interpretation, or a medical device. If you paste or upload medical records into Claude or another hosted AI tool, you may be disclosing medical information to that provider. Review the provider's terms, privacy policy, retention settings, and your own comfort level before adding real records.

## What you will set up

You will create two folders:

```text
Documents/
├── spine-harmony-agent/          # public template repo; no private medical files
└── spine-harmony-private/        # your private workspace; do not upload to GitHub
```

Claude should work inside `spine-harmony-private/`. The public repo is only the instruction and template pack.

## Plain-English overview

Spine Harmony works because Claude can read project instructions and workspace files:

1. `AGENTS.md` tells Claude how a Spine Harmony assistant should behave.
2. `templates/` contains blank starter files for your profile, journal, symptom tracker, Q&A log, and handoff notes.
3. Your private folder stores your real notes and records.
4. Claude helps organize and summarize your files, but it must not make medical decisions.

## Before you begin

You need:

- A computer where you can install apps and use a terminal.
- A Claude account that supports Claude Code, or another Claude-based coding-agent environment.
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

This folder is intentionally separate from the public GitHub repo. Do not push this private folder to GitHub.

## Step 3 — Copy the starter templates

From your `Documents` folder, run:

```bash
cp spine-harmony-agent/AGENTS.md spine-harmony-private/CLAUDE.md
cp spine-harmony-agent/templates/USER.md spine-harmony-private/USER.md
cp spine-harmony-agent/templates/SpineHarmony_Journal.md spine-harmony-private/SpineHarmony_Journal.md
cp spine-harmony-agent/templates/symptom-tracker.md spine-harmony-private/symptom-tracker.md
cp spine-harmony-agent/templates/qa-log.md spine-harmony-private/qa-log.md
cp spine-harmony-agent/templates/handoff.md spine-harmony-private/handoff.md
```

Why this matters:

- `CLAUDE.md` is the project instruction file Claude Code automatically reads.
- The other files are blank/private working files for your own notes.
- Your real information stays in `spine-harmony-private/`, not in the public repo.

If `cp` does not work on Windows PowerShell, use these commands instead:

```powershell
Copy-Item spine-harmony-agent\AGENTS.md spine-harmony-private\CLAUDE.md
Copy-Item spine-harmony-agent\templates\USER.md spine-harmony-private\USER.md
Copy-Item spine-harmony-agent\templates\SpineHarmony_Journal.md spine-harmony-private\SpineHarmony_Journal.md
Copy-Item spine-harmony-agent\templates\symptom-tracker.md spine-harmony-private\symptom-tracker.md
Copy-Item spine-harmony-agent\templates\qa-log.md spine-harmony-private\qa-log.md
Copy-Item spine-harmony-agent\templates\handoff.md spine-harmony-private\handoff.md
```

## Step 4 — Install Claude Code

If you already have Claude Code or your Claude cowork environment installed, skip to Step 5.

Typical Claude Code install path:

```bash
npm install -g @anthropic-ai/claude-code
```

Then sign in:

```bash
claude
```

Follow the login prompts from Anthropic. If your environment uses a hosted Claude coding workspace instead of a local `claude` command, create/open a project and upload or copy the contents of `CLAUDE.md` plus your starter workspace files.

## Step 5 — Start Claude inside the private workspace

Run:

```bash
cd ~/Documents/spine-harmony-private
claude
```

Claude Code should automatically read `CLAUDE.md` from this folder. If it asks whether you trust the folder, choose yes only if the folder is your own private workspace.

## Step 6 — First message to Claude

Paste this as your first prompt:

```text
You are running Spine Harmony in my private workspace. First, read CLAUDE.md, USER.md, SpineHarmony_Journal.md, symptom-tracker.md, qa-log.md, and handoff.md. Then tell me what files are present, what information is still missing, and what I should fill in first. Do not give medical advice or treatment recommendations.
```

Expected result: Claude should summarize the empty starter workspace and ask you to fill in basic non-emergency profile/context fields.

## Step 7 — Fill in your starter files

Start with:

1. `USER.md` — basic profile and preferences.
2. `SpineHarmony_Journal.md` — spine-health timeline and important source notes.
3. `symptom-tracker.md` — pain, sleep, medication, activity, flares/spasms, new symptoms, and comfort measures.
4. `qa-log.md` — questions you asked and source-grounded answers you want to keep.
5. `handoff.md` — concise summary you can paste into a future session.

Use your text editor or ask Claude to help structure blank sections. Do not ask Claude to decide treatment.

## Step 8 — Safe starter prompts

Use prompts like these:

```text
Help me turn these rough spine-history notes into a dated timeline. Preserve uncertainty and do not infer diagnosis.
```

```text
Add this symptom update to symptom-tracker.md: pain 4/10 this morning, slept 6 hours, took no medication, walked 20 minutes, no new symptoms. Then summarize the trend cautiously.
```

```text
Read my journal and symptom tracker. Draft 10 questions I can ask my clinician at the next appointment. Separate source facts from assumptions.
```

```text
Summarize this radiology report in plain English for appointment preparation. Do not diagnose; list terms I should ask the clinician to explain.
```

Avoid prompts like:

```text
What treatment should I choose?
```

```text
Do I need surgery?
```

```text
Is this MRI proof that my pain comes from one structure?
```

```text
Can I ignore these new symptoms?
```

For severe, new, progressive, or worrying symptoms, contact a qualified clinician or emergency services rather than relying on the agent.

## Step 9 — If you want Claude to see the public examples too

Normally, work from `spine-harmony-private/`. If you want Claude to also read the public templates/examples, either:

- paste in the relevant public file content manually; or
- in Claude Code, use the `/add-dir` command to add the public repo folder:

```text
/add-dir ~/Documents/spine-harmony-agent
```

Keep real medical files in the private workspace only.

## Step 10 — Check that private files are not in GitHub

If you used the recommended separate private folder, you are already safer because `spine-harmony-private/` is not the GitHub repo.

If you accidentally worked inside `spine-harmony-agent/`, run this from that folder:

```bash
git status --short
```

If you see real medical files listed, stop before committing or pushing. Move them to `spine-harmony-private/` and make sure `.gitignore` excludes private data.

## Troubleshooting

### Claude says it cannot find the instructions

Check that you are in the private workspace and that `CLAUDE.md` exists:

```bash
cd ~/Documents/spine-harmony-private
ls
```

You should see `CLAUDE.md`.

### Claude forgot the medical boundaries

Ask it to reread the instruction file:

```text
Reread CLAUDE.md and restate the medical and privacy boundaries before continuing.
```

### Claude cannot see your files

Make sure you started Claude from the folder that contains the files:

```bash
cd ~/Documents/spine-harmony-private
claude
```

If using a hosted Claude workspace, upload or attach the files according to that product's instructions.

### You are not comfortable using Terminal

Use the GitHub ZIP download method, create folders with Finder/File Explorer, and copy the template files manually. Then open the private folder in your Claude coding workspace or ask a technical helper to run the short commands above.

### You added real records to the public repo by mistake

Do not commit or push. Move the files out immediately, then check `git status --short`. If private files were already committed or pushed, treat the repository as compromised and seek help removing history; deleting files in a later commit is not enough.

## Beginner safety checklist

Before using real medical data, confirm:

- [ ] I understand Spine Harmony is not medical advice or diagnosis.
- [ ] I understand Claude or another hosted AI provider may process anything I paste or upload.
- [ ] I created a separate `spine-harmony-private/` folder.
- [ ] My private folder is not a GitHub repository.
- [ ] `CLAUDE.md` exists inside the private folder.
- [ ] I copied starter templates into the private folder.
- [ ] I will use the agent for organization, summaries, diary tracking, and clinician questions only.

## What "running" means

Spine Harmony is not a single app with a login screen. In Claude Code/Cowork, it is "running" when:

1. Claude is opened in your private workspace.
2. Claude has read `CLAUDE.md`.
3. Your private workspace contains your journal, tracker, Q&A log, and handoff files.
4. Claude can update or summarize those files while following the safety boundaries.

At that point, you can use it as a patient-side spine-health organization assistant.

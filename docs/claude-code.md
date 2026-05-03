# Claude Code Setup

Spine Harmony can be adapted for Claude Code or Claude-based coding-agent workflows.

Suggested approach:

1. Place the core project instructions from `AGENTS.md` in the Claude Code project instruction context.
2. Keep private patient files in a separate, untracked workspace.
3. Add `.gitignore` rules before creating or importing any real medical files.
4. Use templates from `templates/` to create private local files.
5. Do not ask the model to make clinical decisions; use it to organize notes, draft questions, and summarize source material for clinician review.

Claude Code is not required. Any comparable runtime can be used if it supports file-based context and project instructions.

# Runtime Compatibility

Spine Harmony is runtime-agnostic. It can be adapted to AI-agent systems that support persistent instructions, workspace files, tool use, and ongoing conversation.

Known suitable patterns:

- Hermes Agent skill/workspace configuration;
- OpenClaw agent workspace configuration;
- OpenAI Codex / Copilot-style coding-agent workspace using `AGENTS.md` plus a private local git workspace;
- Claude Code / Claude Cowork project instructions plus a private untracked workspace;
- other AI-agent runtimes with equivalent file access and project instruction support.

For best results, the runtime should preserve enough context to support follow-up Q&A across files and prior notes. If conversation memory is limited, maintain a private `qa-log.md` and handoff summaries.

The runtime is responsible for model selection, tool permissions, data retention behavior, and storage integrations. Users should review the privacy and retention terms of any model or hosted runtime before adding medical data.

For OpenAI Codex-based setups, the simplest safe pattern is:

1. keep this repository as a public template/reference folder;
2. create a separate private workspace folder;
3. initialize that private folder as a local-only git repository, because Codex works best inside a git workspace;
4. copy `AGENTS.md` into the private folder as `AGENTS.md`;
5. copy the starter templates into the private folder;
6. start Codex from the private folder so it reads the project instructions without mixing real medical notes into the public repository.

See `docs/openai-codex.md` for complete novice instructions.

For Claude-based setups, the simplest safe pattern is:

1. keep this repository as a public template/reference folder;
2. create a separate private workspace folder;
3. copy `AGENTS.md` into the private folder as `CLAUDE.md`;
4. copy the starter templates into the private folder;
5. start Claude from the private folder so it reads the project instructions without mixing real medical notes into the public repository.

See `docs/claude-code.md` for complete novice instructions.

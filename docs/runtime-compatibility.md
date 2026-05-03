# Runtime Compatibility

Spine Harmony is runtime-agnostic. It can be adapted to AI-agent systems that support persistent instructions, workspace files, tool use, and ongoing conversation.

Known suitable patterns:

- Hermes Agent skill/workspace configuration;
- OpenClaw agent workspace configuration;
- Claude Code project instructions plus a private untracked workspace;
- other AI-agent runtimes with equivalent file access and project instruction support.

For best results, the runtime should preserve enough context to support follow-up Q&A across files and prior notes. If conversation memory is limited, maintain a private `qa-log.md` and handoff summaries.

The runtime is responsible for model selection, tool permissions, data retention behavior, and storage integrations. Users should review the privacy and retention terms of any model or hosted runtime before adding medical data.

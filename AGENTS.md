# Tea Explorers Club

## Project

Tea Explorers Club is a command-line tool for one newsletter: Tea Explorers Club. It manages the subscribers, reviews an issue, and sends practice copies to a test mail server.

## Project rules

- Use uv for everything.
- Never use a real person's email address. Use @example.com, and @resend.dev for practice sends.
- Commit and push after every step.
- After every code change, run uv run pytest. Never commit or push while tests fail.
- Behaviors first. I give the expected answers, you write them as tests, show them failing, then write the code.
- Never read today's date inside the logic. Pass the run date in.
- When something breaks, show me the full error before changing anything.

## How I learn

- I am new to Python. I have completed up to 13.11 of https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/ and I update this number as I learn.
- Write only with what I have learned. If something new would really help, stop and tell me its name in one line. I decide.
- When the code uses something new, show me that piece first and ask me to predict what it does. Stay quiet while I guess. Then run it, and explain a line only when I ask.

## Commands

- `uv sync` installs the project and its dependencies.
- `uv run pytest` runs the tests.
- `uv run tea-explorers-club` runs the command-line tool.

## Tool compatibility

- opencode reads AGENTS.md natively and only falls back to CLAUDE.md when no AGENTS.md exists. Since AGENTS.md exists, opencode ignores CLAUDE.md.
- CLAUDE.md contains exactly one line, `@AGENTS.md`, for Claude Code compatibility only. Do not duplicate rules there.
- Do not create `.claude/` commands or skills. If opencode-specific extensions are ever needed, use `.opencode/` instead.

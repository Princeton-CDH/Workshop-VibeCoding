# Vibe Coding Starter Kit

Starter kit for the *Vibe Coding Done Right* workshop. Clone it, open it in Windsurf, and you're ready to start exploring research data with AI.

The structure follows the [AGENTS.md](https://agentprotocol.ai) convention and is designed to be portable across AI coding environments — it works with Windsurf/Cascade out of the box and can be adapted for other tools (Cursor, GitHub Copilot, Claude Code) that support project-level AI context files.

**Full tutorial:** https://princeton-cdh.github.io/Workshop-VibeCoding/

---

## Quick Start

```bash
git clone https://github.com/Princeton-CDH/Workshop-VibeCoding.git my-project
```

Open `my-project/` in [Windsurf](https://windsurf.com/download), then in the Cascade panel:

1. `/setup` — creates directories, sets up Python, initializes git
2. `/brief` — downloads your data, fills in your project brief

---

## What's Included

| File                           | Purpose                                              |
| ------------------------------ | ---------------------------------------------------- |
| `AGENTS.md`                    | Project brief template — filled in by `/brief`       |
| `.windsurfrules`               | Analysis style guidelines for Cascade                |
| `.windsurf/workflows/setup.md` | `/setup` workflow                                    |
| `.windsurf/workflows/brief.md` | `/brief` workflow                                    |
| `scripts/notebook.py`          | Marimo notebook skeleton for interactive exploration |

---

*This starter kit and tutorial were developed Jeri Wieringa with assistance from [Claude Code](https://claude.ai).*

---

Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
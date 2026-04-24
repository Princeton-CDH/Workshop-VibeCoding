# Quick Reference

## Workspace and Project Structure

Each project is a clone of the starter kit, renamed and set up independently:

```
moma-collection/          ← cloned from GitHub, renamed to your project
  .windsurf/              ← workflows (/setup, /brief)
  .venv/                  ← Python environment (created by /setup)
  data/                   ← raw source data (NEVER modify)
  outputs/                ← generated files, charts, reports
  scripts/                ← code Cascade writes for you
  AGENTS.md               ← your filled-in project brief
  .windsurfrules          ← analysis style guidelines
  .gitignore
```

To start a new project, clone the starter kit again with a different name.

## Windsurf Essentials

| Action                             | How                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------- |
| Open a folder                      | **File → Open Folder**                                                    |
| Open the terminal                  | **View → Terminal** (or `` Ctrl+` ``)                                     |
| Open Cascade                       | Click the Cascade icon, or `Cmd+L` / `Ctrl+L`                             |
| View files side by side            | Right-click a tab → **Split Right**                                       |
| See git history                    | **Source Control** panel → clock icon, or `git log --oneline` in terminal |
| Undo all changes since last commit | `git checkout .` in the terminal                                          |

## Workflow Commands (type in Cascade)

| Command  | What it does                                                    |
| -------- | --------------------------------------------------------------- |
| `/setup` | Create dirs, set up venv + polars, reset git, make first commit |
| `/brief` | Add data, collect research questions, and fill in `AGENTS.md`   |

## Saving Your Work

Use the **Source Control panel** to commit at any time:

1. Click the Source Control icon in the left sidebar (or `Cmd+Shift+G` / `Ctrl+Shift+G`)
2. Type a short description of what you did
3. Click **Commit All**

## AGENTS.md Template

```markdown
# [Project Name]

## About This Data
- Source: [where the data came from]
- Files: [list your data files and what they contain]
- Known issues: [any quirks or problems you know about]

## Goals
- [What you're trying to accomplish]

## Rules
- Never modify files in data/
- Write all outputs to outputs/
- Write all scripts to scripts/
- Use Python with Polars for data work unless asked otherwise
```

## Terminal Git Commands

If you prefer the command line:

| Command                   | What it does                     |
| ------------------------- | -------------------------------- |
| `git init`                | Start tracking a folder          |
| `git add -A`              | Stage all changes                |
| `git commit -m "message"` | Save a snapshot                  |
| `git log --oneline`       | See your save history            |
| `git diff`                | See what changed since last save |


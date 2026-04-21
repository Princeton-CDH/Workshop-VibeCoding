---
description: Set up this project — creates directories, sets up Python environment, resets git history, and makes the first commit
---

Set up this project. Do each step in order and confirm completion before moving to the next.

## Steps

### 1. Create project directories

Run in the terminal:
```
mkdir -p data outputs scripts
```

### 2. Set up Python virtual environment

Run in the terminal:
```
python3 -m venv .venv
```

### 3. Install core packages

Run in the terminal:
```
.venv/bin/pip install polars
```

Confirm the install succeeded before continuing.

### 4. Reset git history

This removes the starter kit's git history and starts a clean repository for this project.

Run in the terminal:
```
rm -rf .git && git init
```

### 5. Create .gitignore

Create a file at `.gitignore` with this content:

```
# Python
.venv/
__pycache__/
*.pyc
*.pyo
.Python

# OS
.DS_Store
Thumbs.db
```

### 6. Make first commit

Run in the terminal:
```
git add -A && git commit -m "Initial project setup"
```

Tell the user:

> Setup complete. Your project is ready.
>
> - `data/`, `outputs/`, `scripts/` — ready for use
> - `AGENTS.md` — your project brief template
> - `.windsurfrules` — analysis style guidelines, active in every conversation
> - Python virtual environment in `.venv/` with Polars installed
> - Fresh git history initialized
> - `/brief` — run this next to add your data and fill in your project brief
> - `/snapshot` — run this any time you want to save your progress
>
> Run `/brief` to continue.

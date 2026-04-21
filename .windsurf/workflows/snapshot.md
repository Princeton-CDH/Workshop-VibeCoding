---
description: Save a git snapshot — stages all changes and creates a commit with a descriptive message
---

Save a snapshot of the current project state.

## Steps

### 1. Check what's changed

Run in the terminal:
```
git status
```

Show the user which files have been modified or added.

### 2. Ask for a description

Ask the user: "What did you do since your last snapshot? Give me a short description (a few words is fine)."

Wait for their answer before continuing.

### 3. Create the commit

Run in the terminal:
```
git add -A
git commit -m "[use the description the user provided]"
```

### 4. Confirm

Run:
```
git log --oneline -5
```

Tell the user:
> Snapshot saved: "[commit message]"
> 
> Your last 5 snapshots:
> [show the git log output]
>
> To undo everything since this snapshot later, run: `git checkout .`

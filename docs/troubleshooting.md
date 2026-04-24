# Troubleshooting

**Cascade modified my raw data.**
Check with `git diff data/`. If changes were made, restore with `git checkout -- data/`. Then update your `AGENTS.md` to be more explicit: "NEVER modify files in the data/ directory under any circumstances."

**I don't understand the code Cascade wrote.**
That's okay. Ask: "Can you explain what this script does in plain language?" or "Walk me through this step by step." You don't need to understand every line — but you should understand what it's doing at a high level.

**Cascade's output doesn't look right.**
Tell it specifically what's wrong: "The value in this column should be around [X], but your output shows [Y]." The more specific you are, the better Cascade can fix it.

**I want to undo everything since my last commit.**

```
git checkout .
```

This resets all files to your last commit.

**I broke something and I don't know what.**

```
git stash
```

This sets aside all your changes. You can get them back with `git stash pop`, or just start fresh from your last commit.

**The /setup or /brief commands aren't available.**
Make sure you opened the project folder (the one containing `.windsurf/`) in Windsurf. Workflows only appear when Windsurf can see the `.windsurf/workflows/` folder. Use **File → Open Folder** and select the root of your project.


# Vibe Coding Done Right

A hands-on tutorial for researchers getting started with AI-assisted coding.

---

## What You'll Learn

You'll learn to use Windsurf — an AI coding environment that writes code for you based on plain-language descriptions — while following practices that keep your work organized, reproducible, and shareable. By the end, you'll have a working project that cleans and analyzes research data.

**No programming experience required.** You won't write code, but you will type a few commands — we'll walk you through each one. Your main job is to describe what you want clearly and review what the AI produces.

---

## What Is Vibe Coding?

Vibe coding means describing what you want in plain language and letting an AI write the code. You stay in control of the *what* and the *why*; the AI handles the *how*.

This is genuinely powerful. But without a little structure, vibe coding projects become a mess fast. You end up with a folder full of `output_final_v3_REAL.csv` files, no idea which script produced which result, and no way to get back to a clean starting point. You can't share it with a colleague because even *you* don't remember what you did last Tuesday.

This tutorial gives you the minimum structure that prevents that mess — and nothing more. You won't become a software engineer. You'll become someone who can use AI tools withou1t losing track of their own work.

**The mantra: your project folder is your lab notebook.**

Everything that matters — your data, your instructions to the AI, and everything it produces — lives in one folder, organized so that future-you (or a colleague) can understand what happened.

---

## Before You Begin

This tutorial uses a **starter kit** — a small folder pre-configured with everything Cascade needs to work well. Download it once, place it in your Documents folder, and it becomes your project folder.

**Download the starter kit:**

1. Go to [https://github.com/Princeton-CDH/Workshop-VibeCoding](https://github.com/Princeton-CDH/Workshop-VibeCoding)
2. Click the green **Code** button → **Download ZIP**
3. Unzip the downloaded file
4. Rename the folder to `moma-collection`
5. Move it somewhere in your Documents directory

The starter kit contains:

- `AGENTS.md` — a project brief template (you'll fill this in with `/brief`)
- `.windsurfrules` — style guidelines that shape how Cascade approaches analysis: how to handle missing data, how to label charts, how to communicate findings, and more. These apply automatically to every conversation in the project.
- `.windsurf/workflows/setup.md` — a `/setup` command that creates directories, sets up Python, and initializes a fresh git repository
- `.windsurf/workflows/brief.md` — a `/brief` command that downloads your data, collects your research questions, and fills in `AGENTS.md`

---

## Part 1: Setup

### What You Need

- [Windsurf](https://windsurf.com/download) — free to download, works on Mac/Windows/Linux
- A free Windsurf account (you'll create one during install — no paid subscription required to start)

That's it. No extensions to install. The AI assistant (called **Cascade**) is built right into Windsurf.

### Install Windsurf

1. Download Windsurf from [windsurf.com/download](https://windsurf.com/download) and install it
2. Open Windsurf and create a free account when prompted
3. Sign in — you'll land in the editor

You should see a clean editor with a sidebar on the left and a **Cascade** panel available on the right. That's your AI assistant.

!!! info "What if I don't see the Cascade panel?"
    **Tip:** If you don't see the Cascade panel, look for the chat icon in the sidebar or go to **View → Cascade**.


### Getting Oriented

Use **File → Open Folder** to open your project folder. Cascade automatically reads everything in it. You'll work in four areas:

- **File browser (left sidebar)** — your project's files. Click any file to open it.
- **Editor (center)** — view and inspect files; open multiple tabs side by side.
- **Cascade panel** — click the Cascade icon in the sidebar (or use `Cmd+L` / `Ctrl+L`). Type in plain English; Cascade reads your files, writes code, and runs commands.
- **Terminal** — open with **View → Terminal** (or `` Ctrl+` ``). You'll use it for a few commands.

When Cascade creates or modifies files, they appear in the file browser in real time. Click any file to inspect it — this is how you'll review what the AI produces.

### Choosing a Model

Windsurf gives you access to several AI models. Before you start, check which one is active and switch to a good free option if needed.

In the Cascade panel, look for the model name displayed near the bottom of the chat input — it's usually a small label you can click. A menu will appear showing available models.

For this tutorial, select **SWE-1.6** — Windsurf's own coding model, available on the free tier. It's well-suited for data analysis work and doesn't require a paid subscription.

!!! info "What if I don't see SWE-1.6?"
    **What if I don't see SWE-1.6?** The available models depend on your account tier and what Windsurf has released. If SWE-1.6 isn't listed, look for another SWE model (SWE-1, SWE-1.5) or any model marked as free. The tutorial works with any of them.

---

## Part 2: Setting Up Your Project

### Open Your Project in Windsurf

In Windsurf: **File → Open Folder**, navigate to your `moma-collection/` folder, and click **Open**.

### Run /setup

Open the Cascade panel and type:

```
/setup
```

!!! info "Accepting Cascade's Work"
    When Cascade writes code or creates files, it may ask for your approval
    before making changes. This is a safety feature! For each proposed action, you can:

    - **Accept** — let Cascade proceed
    - **Reject** — stop it and give different instructions
    - **Read first** — click on the file to see what Cascade wrote before deciding

    Always pause on anything that touches your `data/` folder. Everything else is recoverable.

Cascade handles the infrastructure:

1. Creates `data/`, `outputs/`, and `scripts/` subfolders
2. Sets up a Python virtual environment (`.venv`) with Polars installed
3. Resets the git history (removes the starter kit's history and starts fresh for your project)
4. Creates a `.gitignore`

!!! info "What's a virtual environment?"
    It's a private copy of Python just for this project. Any packages Cascade installs will live here, contained to this folder, and won't interfere with anything else on your machine.

### Run /brief

Now add your data and fill in your project brief. Type in Cascade:

```
/brief
```

Cascade will walk you through a short conversation:

1. **Asks for your data:** paste the link to the MoMA Artworks CSV:
```
https://media.githubusercontent.com/media/MuseumofModernArt/collection/refs/heads/main/Artworks.csv
```
Cascade downloads it to `data/` for you (the file is large, so this may take a moment)
2. **Asks for your research questions:** what do you want to understand about this data? For example:
```
Who is represented in this collection?
How has it grown over time?
What mediums and departments dominate?
```
3. Fills in `AGENTS.md` with your data source and research questions

Once `/brief` is done, review `AGENTS.md` in the editor — does it capture your project accurately? When you're happy with it, save your first snapshot using the **Source Control panel**:

1. Click the Source Control icon in the left sidebar (or `Cmd+Shift+G` / `Ctrl+Shift+G`)
2. Type a short description — something like `Initial project setup`
3. Click **Commit All**

This saves a checkpoint you can always return to.

### The Golden Rule: Raw Data Is Sacred

Your `data/` folder holds your original source files. **Never modify them.** Every analysis, cleanup, or transformation should read from `data/` and write to `outputs/`. If you accidentally overwrite your source file, you have to re-download it and redo every step from scratch. If it's untouched, you just re-run your scripts on the original.

---

## Part 3: Reviewing Your AGENTS.md

This is the most important file in your project. `AGENTS.md` is a briefing document that Cascade reads at the start of every session. Think of it as onboarding a new colleague: what do they need to know to be useful?

The `/setup` workflow already drafted it from your answers — your data source, downloaded filename, and research questions are already in there. Now you just need to review and refine it.

### Check What Setup Generated

Open `AGENTS.md` in the editor. You should see something like this:

```markdown
# moma-collection

## About This Data
- **Source:** https://github.com/MuseumofModernArt/collection/blob/main/Artworks.csv
- **Files:**
  - `data/Artworks.csv` — MoMA collection metadata for 160,000+ artworks
- **Known issues:** None known yet

## Goals
- Who is represented in this collection?
- How has the collection grown over time?
- What mediums and departments dominate?

## Rules
- Never modify files in `data/`
...
```

**Read it.** Does it capture your questions accurately? If you thought of something new during setup, add it now. If a goal is vague, make it more specific.

### What Makes a Good AGENTS.md

A good briefing answers three questions:

1. **What is this data?** Where it came from, what the columns mean, any quirks or known issues.
2. **What are we trying to do?** Your goals for this project, in plain language.
3. **What are the rules?** Constraints like "don't modify raw data" or "save all outputs to outputs/."

As you learn more about the data, keep this file updated. If you discover that the `Date` column contains inconsistent formats, add that as a known issue. If a new question emerges from your analysis, add it to Goals. The brief is a living document.

### Save Your Work

Once your `AGENTS.md` looks right, commit your changes using the Source Control panel:

1. Click the **Source Control** icon in the left sidebar (or press `Cmd+Shift+G` / `Ctrl+Shift+G`)
2. Type a short description in the message box — something like `Refine project brief`
3. Click **Commit All**

!!! info "Why commit?"
    Each commit is a saved checkpoint in your project history — like saving progress in a video game. You can always rewind to any previous commit if something goes wrong. We'll save after each major step.

---

## Part 4: Exploring Your Data

Now the fun part. You have data, you have a briefing document, and Cascade has context on what the project is about. Let's dig in.

### Start With a Summary

Go back to Cascade. Because your `AGENTS.md` exists, Cascade already has information about your data and goals. Start broad:

```
Give me an overview of data/Artworks.csv — how many rows and columns,
what the columns are, and any immediate observations about the data. Use Polars.
```

Cascade will read the file and report back: row and column counts, column names and types, a sense of what's there. You didn't write any code. That's the whole idea.

### Ask Your First Real Question

Don't wait for a perfect plan — start asking. The MoMA collection has some immediately interesting angles:

```
How has the collection grown over time? Plot the number of artworks
acquired each year using the DateAcquired column. Save it to
outputs/acquisitions-by-year.png
```

Look at the chart. Does the shape make sense? You should see relatively low acquisition numbers in the early decades, growth through the mid-20th century, and spikes around major donations. The 1964 and 1968 spikes are particularly dramatic — that's worth investigating:

```
There's a huge spike in 1968. Can you check what's in the CreditLine column
for those rows? I want to know if it was a single major gift.
```

This back-and-forth is normal — expected, even. **You are the domain expert. Cascade is the code generator.** Your job is to look at outputs and say whether they make sense.



### Review What Cascade Produces

This is the most important habit to build: **look at everything Cascade makes.**

1. **Read the script** — Click on any `.py` file in `scripts/`. You don't need to understand every line, but skim it. Does it seem to be doing what you asked?
2. **Check the output** — Click on charts or CSVs in `outputs/`. Does the result match what you'd expect from your knowledge of this collection?

### Keep Exploring

Choose one or more of the follow-up questions to explore (or ask your own questions):

```
What's the gender breakdown of artists in the collection?
Note that Gender values in this dataset are wrapped in parentheses
like `(male)` and `(female)` — strip those before displaying results.
How many works have unknown gender?
```

```
Which departments have the most works? Create a bar chart.
Save it to outputs/works-by-department.png
```

```
What are the 10 most common mediums? Skip rows where Medium is null.
```

```
Which nationalities are most represented? Show me the top 20.
Note that Nationality values are wrapped in parentheses — strip them for display.
```

Each question might produce a script, a chart, a table, or just a text summary. Everything goes to `outputs/`. You're building up a picture of how the collection is shaped — and your domain knowledge tells you when something looks right or worth questioning.

```
What percentage of works have no nationality recorded for the artist?
Does that vary by department?
```

One thing you'll notice quickly: works with multiple creators store all their names, genders, and nationalities concatenated in a single field — `(male) (female)` or `Eames, Charles, Eames, Ray`. This makes simple grouping imprecise. That's a real data modeling decision MoMA made, and it shapes what questions are easy versus hard to answer. Hitting these edges is a feature, not a failure — it's how you discover what to investigate next.

### Save Your Work

Open the Source Control panel (`Cmd+Shift+G` / `Ctrl+Shift+G`), type `Initial exploration`, and click **Commit All**.

---

## Part 5: From Tool to Workflow

Once you've done a few rounds of exploration, you'll start noticing patterns in what you ask Cascade to do. Some tasks happen once — a chart, a quick count. Others are things you'll want to run again and again. This section shows how to build a reusable lookup tool, display results interactively in a code notebook, and wrap the whole thing in a workflow command.

### Build the Lookup Module

Start by asking Cascade to write a lookup function as a Python module:

```
Write a script called scripts/lookup_artist.py that defines a function
`find_artist_works(name, artworks_path, artists_path=None)`. It should:

- Read Artworks.csv using `pl.read_csv(artworks_path, infer_schema_length=0)`
- Filter rows where the Artist column contains the search name (case-insensitive, partial match)
- Select columns: Title, Date, Medium, Department, AccessionNumber, ConstituentID
- If artists_path is provided, join Artists.csv on ConstituentID to add ArtistBio,
  Nationality, BeginDate, EndDate — ConstituentID is comma-separated for
  multi-artist works, so extract the first value with `.str.split(",").list.first().str.strip_chars()` before joining
- Drop ConstituentID from the final result and return the dataframe
```

Writing it as a function (rather than a command-line script) means the code is easier to resue; in our case, we're going to import it into the notebook and call it directly.

### Add the Artists Dataset

MoMA also publishes `Artists.csv` — biographical data (birth year, death year, nationality) keyed to the same artist IDs used in Artworks. Add it:

```
Download `https://media.githubusercontent.com/media/MuseumofModernArt/collection/refs/heads/main/Artists.csv`
to data/Artists.csv
```

### Create a Marimo Notebook

The starter kit includes a skeleton notebook at `scripts/notebook.py`. Ask Cascade to adapt it:

```
Adapt scripts/notebook.py for artist lookup.
Save as scripts/artist-lookup-notebook.py with these specifics:

- In the imports cell: add `import sys` and `sys.path.insert(0, "scripts")`,
  then `from lookup_artist import find_artist_works`
- Search input: `mo.ui.text(label="Artist name", placeholder="e.g. Picasso")`
- Results cell: assign to an `output` variable in each branch, then
  reference `output` as the last line (do not use `return` for display) —
  if `search.value` is not empty, call
  `find_artist_works(search.value, artworks_path="data/Artworks.csv", artists_path="data/Artists.csv")`
  and set `output = mo.vstack([mo.md(f"**{len(results)} work(s) found**"), mo.table(results)])`;
  otherwise set `output = mo.md("Enter an artist name to search the collection.")`
```

Open it from the terminal — run this yourself, not by asking Cascade:

```
.venv/bin/marimo run scripts/artist-lookup-notebook.py
```

Marimo starts a local web server and opens the notebook in your browser — type a name, results appear as a clean table. The terminal stays busy while it runs; that's normal. Press `Ctrl+C` when you're done to stop it.

If the layout or display isn't quite right, describe what you want. For example:

```
The table is showing all 30 columns. Can you limit it to just Title, Date,
Medium, Department, AccessionNumber, Nationality, and Bio?
```

```
Can you add a count of results at the top — "X works found for [name]"?
```

### Turn It Into a Workflow

Once the notebook works, make it a one-word command. Create `.windsurf/workflows/lookup.md`:

~~~markdown
---
description: Show the command to open the artist lookup notebook
---

Tell the user:

> To open the artist lookup notebook, run this in the terminal:
>
> ```
> .venv/bin/marimo run scripts/artist-lookup-notebook.py
> ```
>
> Marimo will open in your browser. The terminal stays busy while it runs — that's normal. Press Ctrl+C to stop it when you're done.
~~~

Now `/lookup` gives the user the exact command without them having to remember it. Cascade doesn't run it directly — `marimo run` starts a web server that never exits, which would cause Cascade to hang.

**The rule of thumb:** if you've described the same task to Cascade three times, make it a workflow. Good candidates: opening a notebook, running a report, checking data quality.

### Before You Close

- [ ] **Did you commit?** Open Source Control (`Cmd+Shift+G`), type a short description, and click **Commit All**
- [ ] **Is your raw data untouched?** Check that nothing in `data/` was modified
- [ ] **Are outputs in the right place?** Everything Cascade generated should be in `outputs/` or `scripts/`
- [ ] **Is your AGENTS.md still accurate?** If the project goals shifted, update the brief

---

## Where to Go Next

The structure you've built here scales to any research data project. A few natural extensions:

- **Build a collection report** — Ask Cascade to generate a formatted summary of your findings — gender breakdown, department distribution, acquisition trends — saved to `outputs/collection-report.md`
- **Apply this to your own data** — Clone the starter kit again, give it a new name, run `/setup` and `/brief` with your own CSV
- **Share your project** — Push to GitHub so colleagues can see and reproduce your work. Your AGENTS.md tells them everything they need to know to pick up where you left off.

---

## Quick Reference

### Workspace and Project Structure

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

### Windsurf Essentials

| Action                             | How                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------- |
| Open a folder                      | **File → Open Folder**                                                    |
| Open the terminal                  | **View → Terminal** (or `` Ctrl+` ``)                                     |
| Open Cascade                       | Click the Cascade icon, or `Cmd+L` / `Ctrl+L`                             |
| View files side by side            | Right-click a tab → **Split Right**                                       |
| See git history                    | **Source Control** panel → clock icon, or `git log --oneline` in terminal |
| Undo all changes since last commit | `git checkout .` in the terminal                                          |

### Workflow Commands (type in Cascade)

| Command  | What it does                                                    |
| -------- | --------------------------------------------------------------- |
| `/setup` | Create dirs, set up venv + polars, reset git, make first commit |
| `/brief` | Add data, collect research questions, and fill in `AGENTS.md`   |

### Saving Your Work

Use the **Source Control panel** to commit at any time:

1. Click the Source Control icon in the left sidebar (or `Cmd+Shift+G` / `Ctrl+Shift+G`)
2. Type a short description of what you did
3. Click **Commit All**

### AGENTS.md Template

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

### Terminal Git Commands

If you prefer the command line:

| Command                   | What it does                     |
| ------------------------- | -------------------------------- |
| `git init`                | Start tracking a folder          |
| `git add -A`              | Stage all changes                |
| `git commit -m "message"` | Save a snapshot                  |
| `git log --oneline`       | See your save history            |
| `git diff`                | See what changed since last save |

---

## Troubleshooting

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

---

## Going Further: Adding Your Own Workflows

Once you've completed a few projects, you may find yourself giving Cascade the same kinds of instructions over and over. You can save those as workflows — reusable commands you trigger with `/`, just like the `/setup` and `/brief` tasks we started with.

Each workflow is a `.md` file in `.windsurf/workflows/` with a short YAML header:

```markdown
---
description: Run the data quality report
---

Run the data quality report on all files in data/.

Execute: python scripts/data-quality-report.py

Then summarize the findings and compare against the previous report
in outputs/ (if one exists). Flag anything new or changed.
```

Save this as `.windsurf/workflows/check-data.md` and you can type `/check-data` in any Cascade session in this project. No re-explaining.

A good rule of thumb: if you've described the same task to Cascade three times, make it a workflow. Good candidates include data quality checks, standard report formats, and cleanup transformations you apply to new data.
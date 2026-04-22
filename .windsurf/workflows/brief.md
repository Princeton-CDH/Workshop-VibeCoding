---
description: Add data and fill in the project brief — asks for data source, downloads it, collects research questions, and fills in AGENTS.md
---

Set up the project brief and download your data. Do each step in order.

## Steps

### 1. Ask for data source

Ask the user: "What data do you want to explore? Paste a direct link to your file (CSV, JSON, etc.) and I'll download it for you. If you don't have a link yet, just say 'skip' and you can add data later."

Wait for their answer. Store it as DATA_URL.

If the user says "skip", note DATA_URL as empty and move to step 3.

### 2. Download the data

Derive a filename from DATA_URL by taking the last segment of the URL path (e.g., `Artworks.csv` from `.../main/Artworks.csv`). Store it as DATA_FILENAME.

If the URL is a GitHub blob URL (contains `github.com` and `/blob/`), convert it to the raw download URL by replacing `github.com` with `raw.githubusercontent.com` and removing `/blob` from the path.

Run in the terminal:
```
curl -L "[DATA_URL]" -o "data/[DATA_FILENAME]"
```

If the download fails, tell the user what went wrong and ask if they'd like to try a different URL or skip for now.

If successful, confirm: "Downloaded `[DATA_FILENAME]` to `data/`."

### 3. Ask for research questions

Ask the user: "What questions do you want to answer with this data? List as many as you like — these become your project goals."

Wait for their answer. Store the response as RESEARCH_QUESTIONS.

### 4. Update AGENTS.md

Read `AGENTS.md` and rewrite it with the information collected, filling in all placeholders:

- Replace `[Project Name]` in the title with the name of the current folder (run `basename $(pwd)` to get it)
- Remove the HTML comment block at the top
- Under **About This Data**:
  - Set **Source** to DATA_URL (or "Not yet added" if skipped)
  - If data was downloaded, set **Files** to list `data/[DATA_FILENAME]` with a brief description based on the filename and URL
  - Set **Known issues** to "None known yet"
- Under **Goals**, replace the placeholder lines with RESEARCH_QUESTIONS formatted as a bullet list
- Keep the **Rules** section exactly as-is

Write the updated content back to `AGENTS.md`.

### 5. Review before committing

Tell the user:

> Here's what's ready:
>
> - `data/[DATA_FILENAME]` — your source data (or empty `data/` if skipped)
> - `AGENTS.md` — your project brief, filled in with your data and goals
>
> Open `AGENTS.md` and take a look — does it capture your project accurately? If anything needs adjusting, make your edits now. When you're happy with it, use the Source Control panel (`Cmd+Shift+G` / `Ctrl+Shift+G`) to save a snapshot — type a short description and click **Commit All**.
>
> You're ready to start exploring — just ask me a question about your data.

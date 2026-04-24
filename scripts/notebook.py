import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import sys
    import marimo as mo
    import polars as pl
    sys.path.insert(0, "scripts")  # allows importing modules from scripts/
    return mo, pl


@app.cell
def _(pl):
    # TODO: update path for your dataset
    df = pl.read_csv("data/your-file.csv", infer_schema_length=0)
    return (df,)


@app.cell
def _(mo):
    # Text input — update label and placeholder to match your data
    search = mo.ui.text(label="Search", placeholder="Enter a name...")
    search
    return (search,)


@app.cell
def _(df, mo, pl, search):
    # TODO: replace "ColumnName" with the column you want to search
    # Assign output in each branch, then reference it as the last line to display
    if search.value:
        results = df.filter(
            pl.col("ColumnName").str.to_lowercase().str.contains(search.value.lower())
        )
        output = mo.vstack([
            mo.md(f"**{len(results)} result(s)**"),
            mo.ui.table(results),
        ])
    else:
        output = mo.md("Enter a search term above.")
    output

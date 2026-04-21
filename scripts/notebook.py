import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    return mo, pl


@app.cell
def _(pl):
    # TODO: update path and column names for your dataset
    df = pl.read_csv("data/your-file.csv")
    return (df,)


@app.cell
def _(mo):
    # Text input — update label and placeholder to match your data
    search = mo.ui.text(label="Search", placeholder="Enter a name...")
    search
    return (search,)


@app.cell
def _(df, mo, pl, search):
    # Filter rows where a column contains the search term (case-insensitive)
    # TODO: replace "ColumnName" with the column you want to search
    if search.value:
        results = df.filter(
            pl.col("ColumnName").str.to_lowercase().str.contains(search.value.lower())
        )
    else:
        results = df.head(20)

    mo.vstack([
        mo.md(f"**{len(results)} result(s)**"),
        mo.table(results),
    ])

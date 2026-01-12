import pandas as pd

# Datei laden
df = pd.read_csv("sales_messy.csv")

# Spaltennamen vereinheitlichen (falls Leerzeichen o.Ä.)
df.columns = [c.strip() for c in df.columns]

# Erwartete Spalten prüfen
required = {"Sales", "Product Name", "Category"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Fehlende Spalten: {missing}")

# Sales in numerisch umwandeln (z.B. "1,234.56" oder "1.234,56")
def to_number(x):
    if pd.isna(x):
        return pd.NA
    s = str(x).strip()
    # Deutsche Schreibweise -> Punkt als Tausender, Komma als Dezimal
    if s.count(",") == 1 and s.count(".") >= 1:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(",") == 1 and s.count(".") == 0:
        s = s.replace(",", ".")
    return pd.to_numeric(s, errors="coerce")

df["Sales"] = df["Sales"].apply(to_number)

# Grundstatistik
print("\nGesamtübersicht")
print(df[["Sales"]].describe())

# Umsätze pro Kategorie
print("\nUmsatz pro Kategorie")
cat_summary = (
    df.groupby("Category", dropna=False)["Sales"]
      .agg(total_sales="sum", avg_sales="mean", count="count")
      .sort_values("total_sales", ascending=False)
)
print(cat_summary)

# Top-Produkte nach Umsatz
print("\nTop 10 Produkte nach Umsatz")
prod_summary = (
    df.groupby("Product Name", dropna=False)["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)
print(prod_summary)

# Fehlende Werte
print("\nFehlende Werte")
print(df[["Sales", "Product Name", "Category"]].isna().sum())

# Optional: Ergebnisse als CSV speichern
cat_summary.to_csv("category_summary.csv")
prod_summary.to_csv("top_products.csv")

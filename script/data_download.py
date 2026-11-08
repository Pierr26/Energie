import pandas as pd

chemin = "time_series_60min_singleindex.csv"  # chemin du fichier téléchargé

def garder(col):
    return (col == "utc_timestamp"
            or col.endswith("price_day_ahead")
            or col.endswith("load_actual_entsoe_transparency"))

df = pd.read_csv(chemin, usecols=garder, parse_dates=["utc_timestamp"], index_col="utc_timestamp")

# Afficher toutes les colonnes
print("\n========== TOUTES LES COLONNES ==========")

for i, colonne in enumerate(df.columns, start=1):
    print(f"{i}. {colonne}")

# Compter les colonnes
print("\nNombre total de colonnes :", len(df.columns))

# Séparer les catégories
prix = [c for c in df.columns if "price" in c]
charges = [c for c in df.columns if "load" in c]

print("\nNombre de colonnes de prix :", len(prix))
print("Nombre de colonnes de charge :", len(charges))

print("\n========== PRIX DAY AHEAD ==========")
for colonne in prix:
    print(colonne)

print("\n========== DEMANDE ELECTRIQUE ==========")
for colonne in charges:
    print(colonne)
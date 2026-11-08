# Prevision day-ahead du prix de l'electricite en Allemagne

Ce projet predit le prix horaire day-ahead allemand a partir du fichier ENTSO-E `time_series_60min_singleindex.csv`.

## Structure

- `script/forecast_germany.ipynb` : analyse complete et reproductible.
- `script/data_download.py` : inspection des colonnes du fichier source.
- `script/requirements.txt` : dependances Python.
- `script/time_series_60min_singleindex.csv` : donnees brutes locales, ignorees par Git car le fichier est volumineux.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r script/requirements.txt
```

Dans VS Code, selectionner l'environnement `.venv` comme kernel du notebook.

## Donnees

Placer le fichier `time_series_60min_singleindex.csv` dans `script/`. Il n'est pas publie dans GitHub en raison de sa taille.

## Execution

Ouvrir `script/forecast_germany.ipynb` et executer les cellules dans l'ordre. Le notebook :

- utilise `DE_price_day_ahead` ;
- respecte la contrainte day-ahead avec des retards d'au moins 24 heures ;
- compare une baseline J-1, un modele historique et une fenetre glissante de trois ans ;
- calcule MAE, RMSE, sMAPE et l'amelioration relative a la baseline ;
- sauvegarde les resultats regenerables dans `script/outputs/`.

## Limites

Le fichier couvre une longue periode, de fin 2004 a avril 2019, pendant laquelle le marche a evolue. Pour une utilisation operationnelle, ajouter des previsions de demande, de production renouvelable, de meteo, ainsi que les variables de combustible et de capacite disponibles avant la publication day-ahead.
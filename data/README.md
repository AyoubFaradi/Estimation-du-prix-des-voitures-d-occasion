# 📊 Documentation des Données - Car Price Prediction

Ce dossier contient les données brutes et traitées utilisées pour l'entraînement du modèle de prédiction de prix de voitures.

## 📁 Structure des dossiers

```
data/
├── raw/                    # Données brutes originales
│   └── car_data.csv       # Dataset original (non modifié)
├── processed/              # Données nettoyées et transformées
│   └── car_data_cleaned.csv # Dataset prêt pour l'entraînement
└── README.md              # Ce fichier
```

## 📥 Données brutes (`raw/`)

### Fichier : `car_data.csv`

**Description** : Dataset original contenant les informations sur les voitures d'occasion.

**Caractéristiques** :
- **Format** : CSV (Comma-Separated Values)
- **Encodage** : UTF-8
- **Nombre d'enregistrements** : ~6,923 lignes
- **Source** : Dataset de voitures d'occasion (marché indien)

**Colonnes** :

| Colonne | Type | Description | Exemple |
|---------|------|-----------|---------|
| `name` | string | Nom complet de la voiture | "Maruti Swift Dzire VDI" |
| `company` | string | Marque du constructeur | "Maruti", "Hyundai", "Toyota" |
| `model` | string | Modèle de la voiture | "Swift", "i20", "City" |
| `edition` | string | Édition/version du modèle | "VDI", "Sportz Diesel" |
| `year` | integer | Année de fabrication | 2014, 2010, 2006 |
| `owner` | string | Type de propriétaire | "First", "Second", "Third" |
| `fuel` | string | Type de carburant | "Petrol", "Diesel", "CNG", "LPG", "Electric" |
| `seller_type` | string | Type de vendeur | "Individual", "Dealer" |
| `transmission` | string | Type de transmission | "Manual", "Automatic" |
| `km_driven` | integer | Kilométrage parcouru | 145500, 120000 |
| `mileage_mpg` | float | Consommation en miles par gallon | 55.0, 49.7, 41.6 |
| `engine_cc` | float | Cylindrée du moteur en cc | 1248.0, 1498.0 |
| `max_power_bhp` | float | Puissance maximale en bhp | 74.0, 103.52 |
| `torque_nm` | float | Couple en Newton-mètres | 190.0, 250.0 |
| `seats` | float | Nombre de sièges | 5.0 |
| `selling_price` | integer | Prix de vente (en roupies indiennes) | 450000, 370000 |

**Note** : Les prix dans les données brutes sont en **roupies indiennes (INR)**.

## 🔄 Données traitées (`processed/`)

### Fichier : `car_data_cleaned.csv`

**Description** : Dataset nettoyé et transformé, prêt pour l'entraînement du modèle.

**Transformations appliquées** :

1. **Nettoyage des données** :
   - Suppression des valeurs manquantes (NaN)
   - Suppression des doublons éventuels
   - Validation des types de données

2. **Conversion des prix** :
   - Conversion des prix de **roupies indiennes (INR)** vers **Dirhams marocains (MAD)**
   - Application d'un facteur de conversion (approximativement 1 INR ≈ 0.12 MAD)
   - Les prix sont maintenant en MAD pour correspondre au marché marocain

3. **Normalisation** :
   - Formatage cohérent des valeurs numériques
   - Standardisation des valeurs catégorielles

**Caractéristiques** :
- **Format** : CSV
- **Encodage** : UTF-8
- **Nombre d'enregistrements** : ~6,719 lignes (après nettoyage)
- **Prix** : En **Dirhams marocains (MAD)**

**Exemple de transformation** :
```
Prix brut (INR) : 450,000 ₹
Prix nettoyé (MAD) : 54,000 MAD
```

## 📈 Statistiques des données

### Variables catégorielles

- **Marques** : Maruti, Hyundai, Toyota, Ford, BMW, Skoda, Honda, etc.
- **Types de carburant** : Petrol, Diesel, CNG, LPG, Electric
- **Transmission** : Manual, Automatic
- **Propriétaires** : First, Second, Third
- **Type de vendeur** : Individual, Dealer

### Variables numériques

- **Année** : Plage typique de 1990 à 2025
- **Kilométrage** : 0 à 300,000+ km
- **Consommation** : 20 à 60+ mpg
- **Cylindrée** : 500 à 5000+ cc
- **Puissance** : 30 à 500+ bhp
- **Couple** : 50 à 600+ Nm
- **Sièges** : 2 à 10

## 🔍 Qualité des données

### Problèmes potentiels identifiés

- [ ] **Valeurs manquantes** : Certaines colonnes peuvent contenir des NaN
- [ ] **Outliers** : Valeurs extrêmes dans le kilométrage, prix, etc.
- [ ] **Incohérences** : Années futures, kilométrages négatifs
- [ ] **Duplications** : Enregistrements dupliqués possibles

### Métriques de qualité

- **Taux de complétude** : À calculer
- **Taux de valeurs aberrantes** : À analyser
- **Distribution des features** : À visualiser

## 🚀 Utilisation

### Chargement des données brutes

```python
import pandas as pd

# Charger les données brutes
df_raw = pd.read_csv('data/raw/car_data.csv')
print(f"Shape: {df_raw.shape}")
print(df_raw.head())
```

### Chargement des données nettoyées

```python
import pandas as pd

# Charger les données nettoyées
df_clean = pd.read_csv('data/processed/car_data_cleaned.csv')
print(f"Shape: {df_clean.shape}")
print(df_clean.head())
```

### Utilisation dans l'entraînement

Les données nettoyées sont utilisées par le script d'entraînement :

```bash
python src/ml/train_model.py
```

Le script charge automatiquement `data/raw/car_data.csv`, applique les transformations et sauvegarde le modèle.

## 📝 Notes importantes

1. **Prix** : Les prix dans les données brutes sont en roupies indiennes. Ils sont convertis en MAD lors du traitement.

2. **Données sensibles** : Ce dataset ne contient pas d'informations personnelles identifiables.

3. **Mise à jour** : Les données peuvent être mises à jour périodiquement. Vérifiez la date de dernière modification.

4. **Versioning** : Il est recommandé de versionner les datasets avec Git LFS ou DVC pour les gros fichiers.

## 🔐 Confidentialité et licence

- Les données sont utilisées uniquement à des fins éducatives et de démonstration
- Respectez les conditions d'utilisation du dataset original
- Ne partagez pas les données sans autorisation

## 📊 Analyses futures

- [ ] Analyse exploratoire des données (EDA)
- [ ] Visualisation des distributions
- [ ] Détection des outliers
- [ ] Analyse de corrélation entre features
- [ ] Feature engineering avancé
- [ ] Analyse de la dérive des données (data drift)

## 🔗 Ressources

- Documentation du projet : [README.md](../README.md)
- Script d'entraînement : [src/ml/train_model.py](../src/ml/train_model.py)
- Notebook d'analyse : [notebooks/car_price_pipeline.ipynb](../notebooks/car_price_pipeline.ipynb)

---

**Dernière mise à jour** : 2025


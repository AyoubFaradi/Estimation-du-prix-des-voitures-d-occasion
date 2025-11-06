# 🚗 Car Price Prediction - Système de Prédiction de Prix de Voitures

Un système complet de prédiction de prix de voitures d'occasion utilisant le Machine Learning, avec une API REST (FastAPI) et une interface web interactive (Streamlit).

## 📋 Table des matières

- [À propos du projet](#-à-propos-du-projet)
- [Architecture](#-architecture)
- [Stack technique](#-stack-technique)
- [Fonctionnalités](#-fonctionnalités)
- [Structure du projet](#-structure-du-projet)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Métriques et Performance](#-métriques-et-performance)
- [Docker](#-docker)
- [Tests](#-tests)
- [Auteur](#-auteur)

## 🎯 À propos du projet

Ce projet est un système end-to-end de prédiction de prix de voitures d'occasion qui combine :
- **Machine Learning** : Modèle Random Forest pour la prédiction
- **API REST** : Backend FastAPI pour servir les prédictions
- **Interface Web** : Frontend Streamlit pour l'interaction utilisateur
- **Containerisation** : Docker pour le déploiement facile

Le modèle prédit le prix de vente en MAD (Dirham marocain) en fonction de diverses caractéristiques de la voiture (marque, modèle, année, kilométrage, puissance, etc.).

## 🏗️ Architecture

### Architecture globale

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (Streamlit)                     │
│                    Port: 8501                                │
│              Interface utilisateur interactive               │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP Request (JSON)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend API (FastAPI)                    │
│                    Port: 8000                                │
│              /predict, /health endpoints                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Modèle ML (Random Forest)                       │
│         models/car_price_model.joblib                        │
│         Pipeline: Preprocessing + Regressor                  │
└─────────────────────────────────────────────────────────────┘
```

### Flux de données

1. **Entraînement** :
   ```
   Données brutes (CSV) → Nettoyage → Feature Engineering 
   → Preprocessing → Entraînement Random Forest → Modèle sauvegardé
   ```

2. **Prédiction** :
   ```
   Utilisateur (Streamlit) → API FastAPI → Chargement modèle 
   → Preprocessing → Prédiction → Prix estimé (MAD)
   ```

### Composants principaux

- **`src/ml/train_model.py`** : Script d'entraînement du modèle
- **`src/api/main.py`** : Application FastAPI principale
- **`src/api/routers/predict.py`** : Endpoint de prédiction
- **`src/api/model_loader.py`** : Chargement du modèle (lazy loading)
- **`src/frontend/app.py`** : Interface Streamlit
- **`models/car_price_model.joblib`** : Modèle entraîné sauvegardé

## 🛠️ Stack technique

### Backend
- **FastAPI** : Framework web moderne et rapide pour l'API
- **Pydantic** : Validation des données et schémas
- **Pandas** : Manipulation des données
- **Scikit-learn** : Machine Learning (Random Forest, preprocessing)

### Frontend
- **Streamlit** : Interface web interactive et intuitive

### ML & Data
- **Random Forest Regressor** : Modèle de prédiction
- **OneHotEncoder** : Encodage des variables catégorielles
- **StandardScaler** : Normalisation des variables numériques
- **Joblib** : Sauvegarde/chargement du modèle

### DevOps
- **Docker** : Containerisation
- **Docker Compose** : Orchestration des services

## ✨ Fonctionnalités

- ✅ Prédiction de prix en temps réel
- ✅ Interface utilisateur intuitive avec Streamlit
- ✅ API REST documentée (Swagger/OpenAPI)
- ✅ Validation des données d'entrée
- ✅ Containerisation avec Docker
- ✅ Architecture modulaire et extensible
- ✅ Gestion d'erreurs robuste

## 📁 Structure du projet

```
car-price-prediction/
├── data/
│   ├── raw/                    # Données brutes
│   │   └── car_data.csv
│   ├── processed/              # Données nettoyées
│   │   └── car_data_cleaned.csv
│   └── README.md
├── docker/
│   ├── Dockerfile.backend      # Image Docker pour l'API
│   ├── Dockerfile.frontend     # Image Docker pour Streamlit
│   └── docker-compose.yml      # Orchestration des services
├── models/
│   └── car_price_model.joblib  # Modèle entraîné
├── notebooks/
│   └── car_price_pipeline.ipynb # Notebook d'analyse
├── src/
│   ├── api/                    # Backend API
│   │   ├── main.py             # Application FastAPI
│   │   ├── model_loader.py     # Chargement du modèle
│   │   ├── schemas.py          # Schémas Pydantic
│   │   ├── routers/
│   │   │   ├── predict.py      # Endpoint de prédiction
│   │   │   └── health.py       # Endpoint de santé
│   │   └── requirements.txt
│   ├── frontend/               # Frontend Streamlit
│   │   ├── app.py
│   │   └── requirements.txt
│   └── ml/                     # Machine Learning
│       ├── train_model.py      # Script d'entraînement
│       └── utils.py            # Utilitaires ML
├── tests/                      # Tests unitaires
│   ├── test_api.py
│   ├── test_model.py
│   └── test_data.py
├── requirements.txt            # Dépendances principales
├── Makefile                    # Commandes automatisées
└── README.md                   # Ce fichier
```

## 🚀 Installation

### Prérequis

- Python 3.8+
- Docker & Docker Compose (optionnel, pour la containerisation)

### Installation locale

1. **Cloner le repository**
   ```bash
   git clone https://github.com/AyoubFaradi/car-price-prediction.git
   cd car-price-prediction
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   pip install -r src/api/requirements.txt
   pip install -r src/frontend/requirements.txt
   ```

4. **Entraîner le modèle** (si pas déjà fait)
   ```bash
   python src/ml/train_model.py
   ```

## 💻 Utilisation

### Démarrage local

#### Option 1 : Avec Docker (Recommandé)

```bash
cd docker
docker-compose up --build
```

L'API sera disponible sur `http://localhost:8000`
L'interface web sera disponible sur `http://localhost:8501`

#### Option 2 : Sans Docker

**Terminal 1 - Backend API :**
```bash
cd src/api
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend :**
```bash
cd src/frontend
streamlit run app.py
```

### Utilisation de l'API

#### Endpoint de prédiction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "company": "Maruti",
    "model": "Swift",
    "edition": "VDI",
    "year": 2014,
    "owner": "First",
    "fuel": "Diesel",
    "seller_type": "Individual",
    "transmission": "Manual",
    "km_driven": 145500,
    "mileage_mpg": 25.2,
    "engine_cc": 1248.0,
    "max_power_bhp": 74.0,
    "torque_nm": 190.0,
    "seats": 5
  }'
```

**Réponse :**
```json
{
  "estimated_price_MAD": 245000.50
}
```

#### Documentation interactive

Accédez à la documentation Swagger sur : `http://localhost:8000/docs`

### Interface Web

1. Ouvrez votre navigateur sur `http://localhost:8501`
2. Remplissez le formulaire avec les caractéristiques de la voiture
3. Cliquez sur "Prédire le prix 💰"
4. Le prix estimé s'affichera en MAD

## 📊 Métriques et Performance

### Métriques du modèle ML

Les métriques suivantes sont calculées et suivies :

- **R² Score (Coefficient de détermination)** : Mesure la qualité de l'ajustement du modèle
- **MAE (Mean Absolute Error)** : Erreur moyenne absolue en MAD
- **RMSE (Root Mean Squared Error)** : Erreur quadratique moyenne
- **MAPE (Mean Absolute Percentage Error)** : Erreur en pourcentage

### Métriques à implémenter

- [ ] **Tracking des métriques** : Logging automatique des métriques après entraînement
- [ ] **Validation croisée** : K-fold cross-validation pour évaluer la robustesse
- [ ] **Feature importance** : Analyse de l'importance des caractéristiques
- [ ] **Métriques de distribution** : Analyse des résidus et distribution des erreurs
- [ ] **Comparaison de modèles** : Test de différents algorithmes (XGBoost, Gradient Boosting, etc.)

### Métriques API

- [ ] **Latence** : Temps de réponse moyen des endpoints
- [ ] **Throughput** : Nombre de requêtes par seconde
- [ ] **Taux d'erreur** : Pourcentage de requêtes échouées
- [ ] **Monitoring** : Intégration avec Prometheus/Grafana

### Métriques de données

- [ ] **Qualité des données** : Taux de valeurs manquantes, outliers
- [ ] **Distribution des features** : Statistiques descriptives
- [ ] **Drift detection** : Détection de dérive des données

## 🐳 Docker

### Services Docker

Le projet utilise Docker Compose pour orchestrer deux services :

1. **Backend** (`car_api`) : API FastAPI sur le port 8000
2. **Frontend** (`car_ui`) : Interface Streamlit sur le port 8501

### Commandes Docker

```bash
# Démarrer les services
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down

# Reconstruire les images
docker-compose up --build
```

## 🧪 Tests

Exécuter les tests :

```bash
pytest tests/
```

Tests disponibles :
- `test_api.py` : Tests de l'API
- `test_model.py` : Tests du modèle ML
- `test_data.py` : Tests de validation des données

## 🔮 Améliorations futures

- [ ] Ajout de plus de modèles ML (XGBoost, Neural Networks)
- [ ] Interface d'administration pour le monitoring
- [ ] Cache Redis pour améliorer les performances
- [ ] Authentification et autorisation
- [ ] Historique des prédictions
- [ ] Export des résultats en PDF/Excel
- [ ] Intégration CI/CD avec GitHub Actions
- [ ] Déploiement sur cloud (AWS, GCP, Azure)

## 👤 Auteur

**Ayoub Faradi**

- GitHub: [@AyoubFaradi](https://github.com/AyoubFaradi)
- LinkedIn: [in/ayoub-faradi](https://www.linkedin.com/in/ayoub-faradi)

Développeur Web Full Stack | Intelligence Artificielle | Cloud & DevOps

---

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

---

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !


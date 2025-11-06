# =========================
# ✅ src/api/routers/predict.py
# =========================

from fastapi import APIRouter, HTTPException
from src.api.model_loader import load_model
from src.api.schemas import CarFeatures
import pandas as pd

# Création du routeur (c'est CE nom que main.py doit trouver)
router = APIRouter()

# Chargement du modèle sauvegardé (lazy loading)
_model = None

def get_model():
    """Charge le modèle de manière lazy"""
    global _model
    if _model is None:
        try:
            _model = load_model()
        except FileNotFoundError as e:
            raise HTTPException(status_code=500, detail=str(e))
    return _model

@router.post("/predict")
def predict_price(features: CarFeatures):
    """
    Endpoint pour prédire le prix d'une voiture.
    """
    # Charger le modèle
    model = get_model()
    
    # Transformer les données d'entrée en DataFrame
    # Compatible avec Pydantic v1 et v2
    try:
        features_dict = features.model_dump()  # Pydantic v2
    except AttributeError:
        features_dict = features.dict()  # Pydantic v1
    
    data = pd.DataFrame([features_dict])

    # Prédire avec le modèle
    try:
        prediction = model.predict(data)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction: {str(e)}")

    return {"estimated_price_MAD": round(prediction, 2)}

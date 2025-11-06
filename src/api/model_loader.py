import joblib
import os
from pathlib import Path

def load_model(path: str = None):
    """
    Charge le modèle sauvegardé pour la prédiction.
    """
    if path is None:
        # Trouver le chemin du modèle depuis le répertoire du projet
        project_root = Path(__file__).parent.parent.parent
        path = project_root / "models" / "car_price_model.joblib"
        path = str(path)
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Modèle introuvable : {path}")
    return joblib.load(path)

from fastapi import FastAPI
from src.api.routers import predict, health

# Création de l'application FastAPI
app = FastAPI(title="Car Price Prediction API")

# Inclusion des routes
app.include_router(health.router)
app.include_router(predict.router)

# Route racine
@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API de prédiction de prix de voitures 🚗"}

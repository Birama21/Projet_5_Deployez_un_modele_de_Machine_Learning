# main.py
from fastapi import FastAPI
from app.schemas import PredictionInput
from app.model import load_model
import pandas as pd

# =====================
# Initialisation de l'API
# =====================
app = FastAPI(title="API Prédiction Employee Turnover")

# =====================
# Charger le modèle au démarrage
# =====================
model = load_model()

# =====================
# Fonction de prédiction
# =====================
def predict(model, data: PredictionInput):
    # Convertir les données Pydantic en DataFrame
    df = pd.DataFrame([data.dict()])
    # Prédiction binaire
    prediction = model.predict(df)
    return int(prediction[0])

# =====================
# Endpoint /predict
# =====================
@app.post("/predict")
def make_prediction(data: PredictionInput):
    pred = predict(model, data)
    return {"prediction": pred}
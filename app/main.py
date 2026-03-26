# main.py
from fastapi import FastAPI, UploadFile, File
from app.schemas import PredictionInput
from app.model import load_model
import pandas as pd
import io

# =====================
# Initialisation de l'API
# =====================
app = FastAPI(title="API Prédiction Employee Turnover")

# =====================
# Charger le modèle au démarrage
# =====================
model = load_model()

# =====================
# Fonction de prédiction pour une ligne
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

# =====================
# Endpoint /batch_predict pour tout un CSV
# =====================
@app.post("/batch_predict")
def batch_predict(file: UploadFile = File(...)):
    """
    Endpoint pour prédire toutes les lignes d'un CSV envoyé.
    - file: fichier CSV (sans la colonne cible)
    """
    # Lire le CSV en DataFrame
    contents = file.file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8-sig')))
        # Supprimer la colonne target si elle existe
    if "a_quitte_l_entreprise" in df.columns:
        df = df.drop(columns=["a_quitte_l_entreprise"])

    # Prédictions
    preds = model.predict(df)
    
    # Retourner la liste des prédictions en JSON
    return {"predictions": preds.tolist()}
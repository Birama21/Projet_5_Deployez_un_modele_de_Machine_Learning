# main.py
from fastapi import FastAPI, UploadFile, File
from app.schemas import PredictionInput
from app.model import load_model
from app.data_utils import log_prediction
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
# Fonction de prédiction pour une seule ligne
# =====================
def predict(model, data: PredictionInput):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return int(prediction[0])

# =====================
# Endpoint /predict pour une seule entrée
# =====================
@app.post("/predict")
def make_prediction(data: PredictionInput):
    pred = predict(model, data)
    # Log dans la DB
    log_prediction(data.dict(), pred)
    return {"prediction": pred}

# =====================
# Endpoint /batch_predict pour un CSV
# =====================
@app.post("/batch_predict")
def batch_predict(file: UploadFile = File(...)):
    """
    Endpoint pour prédire toutes les lignes d'un CSV envoyé.
    Les inputs et outputs sont logués dans PostgreSQL.
    """
    # Lire le CSV en DataFrame
    contents = file.file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8-sig")))

    # Supprimer la colonne target si elle existe
    if "a_quitte_l_entreprise" in df.columns:
        df = df.drop(columns=["a_quitte_l_entreprise"])

    predictions = []
    for _, row in df.iterrows():
        input_data = row.to_dict()
        pred = int(model.predict(pd.DataFrame([input_data]))[0])
        # Log input + output dans la DB
        log_prediction(input_data, pred)
        predictions.append(pred)

    return {"predictions": predictions}
from fastapi import FastAPI, UploadFile, File
from app.schemas import PredictionInput
from app.model import load_model
from app.data_utils import log_prediction
from app.database import create_tables
import pandas as pd
import io

app = FastAPI(title="API Prédiction Employee Turnover")

# =====================
# Création des tables au démarrage
# =====================
@app.on_event("startup")
def startup():
    create_tables()

# =====================
# Chargement du modèle
# =====================
model = load_model()

# =====================
# Fonction de prédiction
# =====================
def predict(model, data: PredictionInput):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return int(prediction[0])

# =====================
# Endpoint /predict
# =====================
@app.post("/predict")
def make_prediction(data: PredictionInput):
    pred = predict(model, data)

    try:
        log_prediction(data.dict(), pred)
    except Exception as e:
        print("Erreur log DB:", e)

    return {"prediction": pred}

# =====================
# Endpoint /batch_predict
# =====================
@app.post("/batch_predict")
def batch_predict(file: UploadFile = File(...)):
    contents = file.file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8-sig")))

    if "a_quitte_l_entreprise" in df.columns:
        df = df.drop(columns=["a_quitte_l_entreprise"])

    predictions = []

    for _, row in df.iterrows():
        input_data = row.to_dict()
        pred = int(model.predict(pd.DataFrame([input_data]))[0])

        try:
            log_prediction(input_data, pred)
        except Exception as e:
            print("Erreur log DB:", e)

        predictions.append(pred)

    return {"predictions": predictions}
import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("models/model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, data):
    # convertir en DataFrame avec noms de colonnes
    df = pd.DataFrame([data.dict()])
    
    prediction = model.predict(df)
    
    return int(prediction[0])
from fastapi import FastAPI
from app.schemas import PredictionInput
from app.model import load_model, predict

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict_endpoint(data: PredictionInput):
    prediction = predict(model, data)
    return {"prediction": prediction}
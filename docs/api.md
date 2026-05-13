# 🔌 API Documentation

## Base URL
http://127.0.0.1:8000

## Swagger UI
http://127.0.0.1:8000/docs

## OpenAPI Schema
http://127.0.0.1:8000/openapi.json

---

## POST /predict

Prédit le turnover d’un employé.

Body :
{
  "age": 35,
  "salaire": 50000,
  "anciennete": 3
}

Response :
{
  "prediction": 1
}

---

## POST /batch_predict

Prend un CSV en entrée.

Response :
{
  "n_rows": 100,
  "n_predictions": 100,
  "predictions": [0, 1, 0]
}

---

## Workflow

- requête utilisateur
- traitement FastAPI
- prédiction modèle
- retour réponse
- log optionnel en base

---

## Exemple Python

import requests

url = "http://127.0.0.1:8000/predict"

data = {
  "age": 35,
  "salaire": 50000,
  "anciennete": 3
}

response = requests.post(url, json=data)
print(response.json())

---

## Objectif

Exposer un modèle ML via une API simple en production
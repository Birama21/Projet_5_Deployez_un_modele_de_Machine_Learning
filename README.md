# 🚀 Déploiement d’un modèle Machine Learning – Futurisys

API de prédiction de turnover des employés basée sur un modèle de Machine Learning, exposée via FastAPI, conteneurisée avec Docker et déployée avec CI/CD (GitHub Actions + Hugging Face Spaces).

---

## ⚡ Stack technique
FastAPI · Scikit-learn · Docker · PostgreSQL · Pytest · GitHub Actions · Hugging Face Spaces

---

## 📦 Installation

git clone git@github.com:Birama21/Projet_5_Deployez_un_modele_de_Machine_Learning.git  
cd Projet_5_Deployez_un_modele_de_Machine_Learning  

python -m venv venv  
source venv/bin/activate (Mac/Linux)  
venv\Scripts\activate (Windows)  

pip install -r requirements.txt  
uvicorn app.main:app --reload  

---

## 🐳 Docker

docker compose up --build

---

## 🌐 API

Swagger : http://localhost:8000/docs  

### POST /predict
{
  "age": 35,
  "salaire": 50000,
  "anciennete": 3
}

### POST /batch_predict
Upload CSV → retour liste de prédictions

---

## 🧪 Tests

pytest  

---

## 🗄️ Base de données

PostgreSQL pour log des prédictions (désactivé sur Hugging Face si non disponible)

---

## 🔄 CI/CD

CI : tests automatiques via GitHub Actions à chaque push  
CD : déploiement automatique sur Hugging Face Spaces  

---

## 🚀 Déploiement

Local : Uvicorn ou Docker  
Cloud : Hugging Face Spaces (auto deploy via git push)

---

## 📌 Objectif

Déploiement d’un modèle ML en production avec API, tests et automatisation complète CI/CD.
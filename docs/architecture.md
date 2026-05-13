# 🏗️ Architecture du système

## 📌 Vue d’ensemble

Le projet **Futurisys** est une API de Machine Learning permettant de prédire le turnover des employés.

L’architecture repose sur un système simple mais complet intégrant :
- une API FastAPI
- un modèle de Machine Learning
- une base de données PostgreSQL
- une infrastructure Docker
- un pipeline CI/CD

---

## 🧩 Composants du système

### 🔌 API FastAPI
- Expose les endpoints `/predict` et `/batch_predict`
- Transforme les données en DataFrame
- Charge le modèle ML au démarrage
- Retourne les prédictions

---

### 🤖 Modèle Machine Learning
- Modèle de classification supervisée (Scikit-learn)
- Entraîné sur des données RH
- Sauvegardé puis rechargé pour l’inférence

---

### 🗄️ Base de données PostgreSQL

La base de données permet de stocker les prédictions effectuées par l’API.

| Champ        | Type      | Description                    |
|--------------|-----------|--------------------------------|
| id           | INT (PK)  | Identifiant unique             |
| input_data   | JSON      | Données envoyées à l’API       |
| prediction   | INT       | Résultat du modèle (0 ou 1)    |
| created_at   | TIMESTAMP | Date de la prédiction          |

---

### 🐳 Docker
- Conteneurisation de l’application
- Environnement reproductible
- Simplifie le déploiement local et cloud

---

### 🔄 CI/CD (GitHub Actions)
- Exécution des tests à chaque push
- Validation du code
- Déploiement automatique sur Hugging Face Spaces

---

## 🔁 Flux de données

1. L’utilisateur envoie une requête à l’API
2. FastAPI transforme les données en DataFrame
3. Le modèle ML génère une prédiction
4. La réponse est renvoyée à l’utilisateur
5. La prédiction est enregistrée en base de données (optionnel)

---

## 📊 Diagramme UML - Base de données

```mermaid
erDiagram
    PREDICTIONS {
        int id PK
        json input_data
        int prediction
        datetime created_at
    }
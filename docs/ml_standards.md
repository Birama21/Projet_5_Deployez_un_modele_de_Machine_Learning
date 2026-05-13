# 📏 ML & Code Standards

## 🧱 Objectif

Ce document définit les bonnes pratiques utilisées dans le projet afin d’assurer :
- la qualité du code
- la reproductibilité des expériences
- la maintenabilité du modèle
- la stabilité en production

---

# 💻 Standards de code

## 📌 Style

- Respect de la norme PEP8
- Indentation : 4 espaces
- Variables en snake_case
- Classes en CamelCase
- Fonctions courtes et lisibles

---

## 📁 Organisation du projet

Structure du projet :

- app/ → API FastAPI
- models/ → modèles ML
- tests/ → tests unitaires et fonctionnels
- data/ → datasets (si applicable)

---

## 🧠 Bonnes pratiques

- Séparer logique métier et API
- Éviter les fonctions trop longues
- Ajouter des docstrings si nécessaire
- Réutiliser le code au maximum

---

# 🌿 Git & versioning

## 📌 Branches

- main → production
- develop → développement
- feature/* → nouvelles fonctionnalités
- bugfix/* → corrections
- hotfix/* → corrections urgentes

---

## 📌 Commits

Format recommandé :

- feat: nouvelle fonctionnalité
- fix: correction de bug
- docs: documentation
- refactor: amélioration du code

Exemple :
feat: ajout endpoint /predict

---

# 🤖 Standards Machine Learning

## 📊 Données

- nettoyage des données
- séparation train / test
- encodage des variables catégorielles si nécessaire

---

## 🏋️ Entraînement

- utilisation de pipelines reproductibles
- seed fixée pour reproductibilité
- versionnage des datasets si possible

---

## 📈 Évaluation

Métriques utilisées :

- Accuracy
- Precision
- Recall
- F1-score

---

## 💾 Modèles

- sauvegarde via joblib ou pickle
- séparation entraînement / inférence
- versionnage des modèles si nécessaire

---

# 🧪 Tests

- tests unitaires avec pytest
- fichiers nommés test_*.py
- exécution automatique via CI/CD

---

# 🚀 CI/CD

- tests automatiques à chaque push
- validation du code
- déploiement automatique si tests OK

---

# 🎯 Objectif

Garantir un projet :
- propre
- reproductible
- maintenable
- prêt pour production

## 🔄 Protocole de mise à jour du modèle

Afin de garantir la performance du modèle dans le temps, un protocole de mise à jour régulière est mis en place.

### 📅 Fréquence de mise à jour
- Réentraînement mensuel du modèle
- Réentraînement déclenché si baisse de performance détectée

### 📊 Surveillance des performances
- Suivi des métriques (accuracy, precision, recall)
- Détection de dérive des données (data drift)

### 🔁 Processus de mise à jour
1. Collecte des nouvelles données
2. Nettoyage et prétraitement
3. Réentraînement du modèle
4. Évaluation des performances
5. Validation du modèle
6. Déploiement en production

### 🧪 Validation
- Comparaison avec le modèle précédent
- Validation sur un jeu de test indépendant

### 🚀 Déploiement
- Mise à jour via pipeline CI/CD
- Versionnement du modèle
- Possibilité de rollback en cas de problème

## 🔄 Protocole de mise à jour du modèle

Afin de garantir la performance et la fiabilité du modèle dans le temps, un protocole de mise à jour régulière est mis en place.

---

### 📅 1. Fréquence de mise à jour

- Réentraînement planifié du modèle : **mensuel**
- Réentraînement déclenché si :
  - baisse des performances (accuracy, F1-score)
  - dérive des données (data drift détecté)
  - ajout de nouvelles données significatives

---

### 📊 2. Suivi des performances

Les performances du modèle sont surveillées via :

- Accuracy
- Precision / Recall
- F1-score
- Analyse des erreurs de prédiction

---

### 📦 3. Gestion des données

- Collecte continue de nouvelles données
- Nettoyage et validation des données
- Stockage dans la base PostgreSQL (`datasets`, `model_inputs`, `model_outputs`)

---

### 🔁 4. Processus de réentraînement

1. Extraction des nouvelles données
2. Prétraitement et feature engineering
3. Réentraînement du modèle
4. Évaluation sur un jeu de test
5. Comparaison avec le modèle actuel

---

### ✅ 5. Validation du modèle

Avant déploiement :

- comparaison avec la version précédente
- validation des métriques minimales
- contrôle des biais éventuels

---

### 🚀 6. Déploiement

- versionning du modèle (ex: v1, v2…)
- déploiement via pipeline CI/CD
- possibilité de rollback en cas de régression

---

### 🧠 7. Objectif

Garantir un modèle :

- performant dans le temps
- adapté aux nouvelles données
- fiable en production
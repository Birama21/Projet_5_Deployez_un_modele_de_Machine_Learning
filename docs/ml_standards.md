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
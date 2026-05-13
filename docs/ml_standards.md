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
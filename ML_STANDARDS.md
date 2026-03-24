# ML & Code Standards – Projet Futurisys

Ce document définit les standards de développement et d’expérimentation utilisés dans ce projet afin de garantir la qualité, la lisibilité et la reproductibilité du code.

---

# 🧱 1. Standards de code

## 📌 Style de code
- Respect des conventions **PEP8**
- Indentation : 4 espaces
- Nommage des variables en `snake_case`
- Nommage des classes en `CamelCase`
- Fonctions courtes et explicites

## 📌 Organisation du code
Le projet est structuré de manière modulaire :

- `app/` : API FastAPI
- `models/` : modèles de Machine Learning
- `tests/` : tests unitaires et fonctionnels
- `data/` : jeux de données (si applicable)

## 📌 Bonnes pratiques
- Séparer la logique métier de l’API
- Éviter les fonctions trop longues
- Documenter les fonctions si nécessaire (docstrings)
- Réutiliser le code (éviter les duplications)

---

# 🌿 2. Standards Git

## 📌 Branches
- `main` : version stable en production
- `develop` : intégration des fonctionnalités
- `feature/<nom>` : nouvelles fonctionnalités
- `bugfix/<nom>` : corrections de bugs
- `hotfix/<nom>` : corrections urgentes

## 📌 Commits
- Commits clairs et descriptifs
- Convention recommandée :
  - `feat:` ajout d’une fonctionnalité
  - `fix:` correction de bug
  - `docs:` documentation
  - `refactor:` amélioration du code sans changement fonctionnel

Exemple :


---

# 🤖 3. Standards d’expérimentation Machine Learning

## 📌 Préparation des données
- Nettoyage des données en amont
- Séparation des données en :
  - train
  - test
- Encodage des variables catégorielles si nécessaire

## 📌 Entraînement
- Utilisation de pipelines reproductibles
- Fixation des seeds pour reproductibilité
- Versionnage des datasets si possible

## 📌 Évaluation
- Utilisation de métriques adaptées au problème :
  - Classification : accuracy, precision, recall, F1-score
  - Régression : RMSE, MAE, R²

## 📌 Validation
- Validation croisée si nécessaire
- Évaluation sur un dataset de test indépendant

---

# 💾 4. Gestion des modèles

- Sauvegarde des modèles entraînés (pickle / joblib)
- Versionnage des modèles si nécessaire
- Séparation entre entraînement et inférence

---

# 🔁 5. Reproductibilité

- Version Python fixée (ex: 3.10)
- Gestion des dépendances via `requirements.txt`
- Environnement isolé (virtualenv / uv / poetry)
- Seeds fixées pour les expériences

---

# 🧪 6. Tests

- Utilisation de Pytest
- Tests dans le dossier `tests/`
- Fichiers nommés `test_*.py`
- Exécution automatique via CI/CD

---

# 🚀 7. CI/CD

- Pipeline automatisé via GitHub Actions
- Installation des dépendances
- Exécution des tests à chaque push / pull request
- Validation avant fusion des branches

---

# 📌 Objectif

Ces standards garantissent :
- un code propre et maintenable
- des expérimentations reproductibles
- une collaboration efficace
- une mise en production fiable
# ML & Code Standards – Projet Futurisys

Ce document définit les standards de développement, d’expérimentation et de déploiement utilisés dans ce projet afin de garantir la qualité, la reproductibilité et la maintenabilité.

---

# 🧱 1. Standards de code

## 📌 Style de code
- Respect des conventions **PEP8**
- Indentation : 4 espaces
- Variables en `snake_case`
- Classes en `CamelCase`
- Fonctions courtes, claires et avec une seule responsabilité

## 📌 Organisation du projet
- `app/` : API FastAPI (routes + logique métier)
- `models/` : modèle ML (sauvegarde et chargement)
- `tests/` : tests unitaires et fonctionnels
- `data/` : datasets (optionnel)

## 📌 Bonnes pratiques
- Séparer API et logique Machine Learning
- Éviter la duplication de code
- Utiliser des fonctions réutilisables
- Ajouter des docstrings sur les fonctions importantes

---

# 🌿 2. Standards Git

## 📌 Branches
- `main` : version stable (production)
- `feature/*` : nouvelles fonctionnalités
- `bugfix/*` : corrections de bugs
- `hotfix/*` : corrections urgentes

## 📌 Commits
Les messages de commit doivent être clairs et explicites.

Convention recommandée :
- `feat:` ajout de fonctionnalité
- `fix:` correction de bug
- `docs:` documentation
- `refactor:` amélioration du code sans changement fonctionnel

Exemple :
feat: ajout endpoint batch_predict

---

# 🤖 3. Standards Machine Learning

## 📌 Données
- Nettoyage des données avant entraînement
- Gestion des valeurs manquantes
- Encodage des variables catégorielles si nécessaire

## 📌 Entraînement
- Pipeline reproductible
- Séparation train / test
- Seed fixée pour reproductibilité

## 📌 Évaluation
- Classification : accuracy, precision, recall, F1-score

---

# 💾 4. Gestion du modèle

- Modèle sauvegardé avec `joblib` ou `pickle`
- Chargé au démarrage de l’API FastAPI
- Séparation stricte entre entraînement et inférence

---

# 🔁 5. Reproductibilité

- Python version 3.11
- Dépendances dans `requirements.txt`
- Environnement isolé (venv ou Docker)
- Seeds fixées pour stabilité des résultats

---

# 🧪 6. Tests

- Tests avec Pytest
- Dossier `tests/`
- Fichiers `test_*.py`
- Exécution automatisée via CI/CD

---

# 🚀 7. CI/CD & Déploiement

## CI (GitHub Actions)
- Installation des dépendances
- Exécution des tests à chaque push
- Validation automatique du code

## CD (Hugging Face Spaces)
- Déploiement automatique via push sur `main`
- Mise à jour automatique de l’API

---

# 📌 Objectif

Ce projet garantit :
- un code propre et structuré
- une API stable et reproductible
- un workflow CI/CD automatisé
- un déploiement fiable en production
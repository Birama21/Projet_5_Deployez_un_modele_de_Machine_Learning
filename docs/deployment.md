# 🤖 Modèle Machine Learning

## 📌 Objectif

Le modèle a pour objectif de prédire le **turnover des employés** (départ ou maintien dans l’entreprise) à partir de variables RH.

---

## 🧠 Type de problème

Il s’agit d’un problème de **classification binaire** :
- 0 → l’employé reste
- 1 → l’employé quitte l’entreprise

---

## 📊 Features utilisées

Les variables principales utilisées pour l’entraînement sont :

- âge
- salaire
- ancienneté
- (autres variables RH selon dataset)

---

## ⚙️ Algorithme utilisé

Le modèle est basé sur **Scikit-learn**.

Exemples possibles :
- RandomForestClassifier
- Logistic Regression
- Gradient Boosting

---

## 🏋️ Entraînement

Étapes du training :

1. Nettoyage des données
2. Encodage des variables catégorielles
3. Séparation train / test
4. Entraînement du modèle
5. Évaluation des performances
6. Sauvegarde du modèle (pickle / joblib)

---

## 📈 Évaluation du modèle

Les métriques utilisées :

- Accuracy
- Precision
- Recall
- F1-score

---

## 💾 Sauvegarde

Le modèle entraîné est sauvegardé pour être utilisé en production dans l’API.

Format :
- `.pkl` ou `.joblib`

---

## 🚀 Utilisation en production

Le modèle est chargé au démarrage de l’API FastAPI et utilisé pour générer des prédictions en temps réel.

---

## 🔁 Pipeline ML

Données → Prétraitement → Modèle → Prédiction → API → Utilisateur

---

## 🎯 Objectif final

Avoir un modèle :
- stable
- reproductible
- performant
- intégré dans une API de production
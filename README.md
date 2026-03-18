# Projet_5_D-ployez_un_mod-le_de_Machine_Learning
deployez un modèle ML
# Déploiement d’un modèle Machine Learning – Futurisys

Ce projet a pour objectif de déployer un modèle de Machine Learning en production pour **Futurisys**, une entreprise souhaitant rendre ses modèles opérationnels et accessibles via une API performante.

Le projet inclut :  
- Une API REST exposant le modèle ML via **FastAPI**.  
- Tests unitaires et fonctionnels avec **Pytest**.  
- Gestion de la base de données **PostgreSQL**.  
- Pipeline **CI/CD** pour automatiser tests et déploiement.

---

## Table des matières
1. [Prérequis](#prérequis)  
2. [Installation](#installation)  
3. [Structure du projet](#structure-du-projet)  
4. [Utilisation de l’API](#utilisation-de-lapi)  
5. [Tests](#tests)  
6. [Déploiement](#déploiement)  
7. [Base de données](#base-de-données)  
8. [Pipeline CI/CD](#pipeline-cicd)  
9. [Contribuer](#contribuer)  
10. [Licence](#licence)  
11. [Conventions Git / Branches](#conventions-git--branches)

---

## Prérequis
- Python ≥ 3.12  
- PostgreSQL ≥ 15  
- Git  
- Virtualenv ou Conda 

## Installation 
- git clone git@github.com:Birama21 Projet_5_Deployez_un_modele_de_Machine_Learning.git
- use ssh key 

## Conventions Git / Branches

- main : branche principale stable,
- feature/<nom-fonctionnalité> : nouvelle fonctionnalité,
- bugfix/<nom-du-bug> : correction de bug,
- hotfix/<nom-du-hotfix> : corrections urgentes,
- release/<version> : pour préparer une version à publier
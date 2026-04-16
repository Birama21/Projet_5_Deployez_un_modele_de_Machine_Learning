# app/models.py

from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# =====================
# Table pour le dataset complet
# =====================
class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer)
    genre = Column(Integer)
    statut_marital = Column(String)
    poste = Column(String)
    nombre_experiences_precedentes = Column(Integer)
    annee_experience_totale = Column(Integer)
    annees_dans_l_entreprise = Column(Integer)
    annees_dans_le_poste_actuel = Column(Integer)
    nombre_participation_pee = Column(Integer)
    nb_formations_suivies = Column(Integer)
    distance_domicile_travail = Column(Float)
    niveau_education = Column(Integer)
    domaine_etude = Column(String)
    frequence_deplacement = Column(String)
    annees_depuis_la_derniere_promotion = Column(Integer)
    annes_sous_responsable_actuel = Column(Integer)
    satisfaction_employee_environnement = Column(Integer)
    note_evaluation_precedente = Column(Integer)
    niveau_hierarchique_poste = Column(Integer)
    satisfaction_employee_nature_travail = Column(Integer)
    satisfaction_employee_equipe = Column(Integer)
    satisfaction_employee_equilibre_pro_perso = Column(Integer)
    note_evaluation_actuelle = Column(Integer)
    heure_supplementaires = Column(Float)
    augementation_salaire_precedente = Column(Float)
    Aug_net = Column(Float)
    Rat_Rev_Aentr = Column(Float)
    a_quitte_l_entreprise = Column(Boolean)

# =====================
# Table pour stocker les inputs envoyés au modèle
# =====================
class ModelInput(Base):
    __tablename__ = "model_inputs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer)
    genre = Column(Integer)
    statut_marital = Column(String)
    poste = Column(String)
    nombre_experiences_precedentes = Column(Integer)
    annee_experience_totale = Column(Integer)
    annees_dans_l_entreprise = Column(Integer)
    annees_dans_le_poste_actuel = Column(Integer)
    nombre_participation_pee = Column(Integer)
    nb_formations_suivies = Column(Integer)
    distance_domicile_travail = Column(Float)
    niveau_education = Column(Integer)
    domaine_etude = Column(String)
    frequence_deplacement = Column(String)
    annees_depuis_la_derniere_promotion = Column(Integer)
    annes_sous_responsable_actuel = Column(Integer)
    satisfaction_employee_environnement = Column(Integer)
    note_evaluation_precedente = Column(Integer)
    niveau_hierarchique_poste = Column(Integer)
    satisfaction_employee_nature_travail = Column(Integer)
    satisfaction_employee_equipe = Column(Integer)
    satisfaction_employee_equilibre_pro_perso = Column(Integer)
    note_evaluation_actuelle = Column(Integer)
    heure_supplementaires = Column(Float)
    augementation_salaire_precedente = Column(Float)
    Aug_net = Column(Float)
    Rat_Rev_Aentr = Column(Float)

    # ✅ timestamp propre (timezone + PostgreSQL)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

# =====================
# Table pour stocker les prédictions du modèle
# =====================
class ModelOutput(Base):
    __tablename__ = "model_outputs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    input_id = Column(Integer, nullable=False)
    prediction = Column(Integer)

    # ✅ timestamp propre
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
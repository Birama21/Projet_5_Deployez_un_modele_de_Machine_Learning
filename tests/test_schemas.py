import pytest
from pydantic import ValidationError
from app.schemas import PredictionInput

def test_prediction_input_valid():
    data = {
        "age": 30,
        "genre": 1,
        "statut_marital": "Single",
        "poste": "Engineer",
        "nombre_experiences_precedentes": 2,
        "annee_experience_totale": 5,
        "annees_dans_l_entreprise": 3,
        "annees_dans_le_poste_actuel": 2,
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 3,
        "distance_domicile_travail": 10.5,
        "niveau_education": 3,
        "domaine_etude": "IT",
        "frequence_deplacement": "Rarely",
        "annees_depuis_la_derniere_promotion": 1,
        "annes_sous_responsable_actuel": 2,
        "satisfaction_employee_environnement": 4,
        "note_evaluation_precedente": 3,
        "niveau_hierarchique_poste": 2,
        "satisfaction_employee_nature_travail": 4,
        "satisfaction_employee_equipe": 4,
        "satisfaction_employee_equilibre_pro_perso": 3,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": 5.0,
        "augementation_salaire_precedente": 2.5,
        "Aug_net": 1000.0,
        "Rat_Rev_Aentr": 0.2
    }

    obj = PredictionInput(**data)

    assert obj.age == 30
    assert obj.poste == "Engineer"


def test_prediction_input_missing_field():
    data = {
        "age": 30
    }

    with pytest.raises(ValidationError):
        PredictionInput(**data)


def test_prediction_input_wrong_type():
    data = {
        "age": "trente",
        "genre": 1,
        "statut_marital": "Single",
        "poste": "Engineer",
        "nombre_experiences_precedentes": 2,
        "annee_experience_totale": 5,
        "annees_dans_l_entreprise": 3,
        "annees_dans_l_entreprise": 3,
        "annees_dans_le_poste_actuel": 2,
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 3,
        "distance_domicile_travail": 10.5,
        "niveau_education": 3,
        "domaine_etude": "IT",
        "frequence_deplacement": "Rarely",
        "annees_depuis_la_derniere_promotion": 1,
        "annes_sous_responsable_actuel": 2,
        "satisfaction_employee_environnement": 4,
        "note_evaluation_precedente": 3,
        "niveau_hierarchique_poste": 2,
        "satisfaction_employee_nature_travail": 4,
        "satisfaction_employee_equipe": 4,
        "satisfaction_employee_equilibre_pro_perso": 3,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": 5.0,
        "augementation_salaire_precedente": 2.5,
        "Aug_net": 1000.0,
        "Rat_Rev_Aentr": 0.2
    }

    with pytest.raises(ValidationError):
        PredictionInput(**data)
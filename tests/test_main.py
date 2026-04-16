import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# =========================
# 🎭 MOCK log_prediction
# =========================
def fake_log_prediction(input_data, prediction):
    return None


# on remplace la vraie fonction par fake
import app.main
app.main.log_prediction = fake_log_prediction


# =========================
# 🧪 TEST /predict
# =========================
def test_predict_endpoint():
    payload = {
        "age": 30,
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

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "prediction" in response.json()


# =========================
# 🧪 TEST /batch_predict
# =========================
def test_batch_predict_endpoint():
    csv_data = """age,genre,statut_marital,poste,nombre_experiences_precedentes,annee_experience_totale,annees_dans_l_entreprise,annees_dans_l_entreprise,annees_dans_le_poste_actuel,nombre_participation_pee,nb_formations_suivies,distance_domicile_travail,niveau_education,domaine_etude,frequence_deplacement,annees_depuis_la_derniere_promotion,annes_sous_responsable_actuel,satisfaction_employee_environnement,note_evaluation_precedente,niveau_hierarchique_poste,satisfaction_employee_nature_travail,satisfaction_employee_equipe,satisfaction_employee_equilibre_pro_perso,note_evaluation_actuelle,heure_supplementaires,augementation_salaire_precedente,Aug_net,Rat_Rev_Aentr
30,1,Single,Engineer,2,5,3,3,2,1,3,10.5,3,IT,Rarely,1,2,4,3,2,4,4,3,4,5.0,2.5,1000.0,0.2
"""

    files = {
        "file": ("test.csv", csv_data, "text/csv")
    }

    response = client.post("/batch_predict", files=files)

    assert response.status_code == 200
    assert "predictions" in response.json()
    assert isinstance(response.json()["predictions"], list)
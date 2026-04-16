import pytest
from app import model as model_module


# =========================
# 🎭 Fake model (mock)
# =========================
class FakeModel:
    def predict(self, X):
        return [1]


# =========================
# ✅ Test de la fonction predict()
# =========================
def test_predict_function():
    fake_model = FakeModel()

    # Fake input (comme ton schema)
    class FakeInput:
        def dict(self):
            return {
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

    fake_input = FakeInput()

    result = model_module.predict(fake_model, fake_input)

    assert result == 1


# =========================
# ✅ Test load_model (mock joblib)
# =========================
def test_load_model(monkeypatch):
    class FakeModel:
        pass

    def fake_load(path):
        return FakeModel()

    # on remplace joblib.load par fake_load
    monkeypatch.setattr("joblib.load", fake_load)

    model = model_module.load_model()

    assert isinstance(model, FakeModel)
import pytest
import pandas as pd
from app import data_utils


# =========================
# 🎭 Fake Session
# =========================
class FakeSession:
    def __init__(self):
        self.add_count = 0
        self.commit_count = 0
        self.refresh_called = False
        self.closed = False
        self.rollback_called = False

    def add(self, obj):
        self.add_count += 1

    def commit(self):
        self.commit_count += 1

    def refresh(self, obj):
        self.refresh_called = True
        obj.id = 1  # simulate DB generated id

    def close(self):
        self.closed = True

    def rollback(self):
        self.rollback_called = True


# =========================
# 🧪 TEST log_prediction
# =========================
def test_log_prediction(monkeypatch):

    fake_session = FakeSession()

    monkeypatch.setattr(data_utils, "SessionLocal", lambda: fake_session)

    input_data = {
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

    data_utils.log_prediction(input_data, 1)

    assert fake_session.add_count == 2
    assert fake_session.commit_count == 2
    assert fake_session.refresh_called is True
    assert fake_session.closed is True
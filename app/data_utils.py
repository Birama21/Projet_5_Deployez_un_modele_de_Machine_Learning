# app/data_utils.py
import pandas as pd
from app.database import SessionLocal
from app.models import Dataset, ModelInput, ModelOutput

def insert_csv_to_db(csv_path: str):
    """
    Insère toutes les lignes d'un CSV dans la table datasets.
    """
    df = pd.read_csv(csv_path)
    session = SessionLocal()
    try:
        for _, row in df.iterrows():
            dataset_row = Dataset(**row.to_dict())
            session.add(dataset_row)
        session.commit()
        print("CSV inséré avec succès !")
    except Exception as e:
        session.rollback()
        print("Erreur lors de l'insertion du CSV :", e)
    finally:
        session.close()


def log_prediction(input_data: dict, prediction: int):
    """
    Logue un input et sa prédiction dans les tables model_inputs et model_outputs.
    """
    session = SessionLocal()
    try:
        # Sauvegarder input
        input_row = ModelInput(**input_data)
        session.add(input_row)
        session.commit()  # commit pour obtenir l'id
        session.refresh(input_row)

        # Sauvegarder output
        output_row = ModelOutput(input_id=input_row.id, prediction=prediction)
        session.add(output_row)
        session.commit()
        print("Prediction loguée avec succès !")
    except Exception as e:
        session.rollback()
        print("Erreur lors du log de la prediction :", e)
    finally:
        session.close()
# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

# =====================
# Connexion à PostgreSQL
# =====================
DB_USER = "postgres"
DB_PASSWORD = quote_plus("Birama.21")
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "employee_db"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# =====================
# Engine
# =====================
engine = create_engine(
    DATABASE_URL,
    echo=True  # logs SQL
)

# =====================
# Session
# =====================
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# =====================
# Création des tables
# =====================
def create_tables():
    from app.models import Base  # ⚠️ IMPORTANT : on importe ici

    Base.metadata.create_all(bind=engine)
    print("Tables créées avec succès !")
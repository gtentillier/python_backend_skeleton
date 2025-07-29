from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
  """
  Fournit une session de base de données pour les dépendances FastAPI.

  Yields:
      Session: Session SQLAlchemy.
  """
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

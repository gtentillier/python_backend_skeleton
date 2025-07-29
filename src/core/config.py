from pydantic_settings import BaseSettings  # pip install pydantic-settings


class Settings(BaseSettings):
  """Configuration globale de l'application."""

  # Application
  APP_NAME: str = "My FastAPI App"
  DEBUG: bool = False
  VERSION: str = "1.0.0"

  # Base de données
  DATABASE_URL: str = "postgresql://user:password@localhost/dbname"

  # Sécurité
  SECRET_KEY: str = "your_secret_key"
  ALGORITHM: str = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

  # Autres configurations
  CORS_ORIGINS: list[str] = ["http://localhost:3000"]

  class Config:
    env_file = ".env"


# Instance unique des paramètres
settings = Settings()

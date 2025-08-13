from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt  # pip install python-jose
from fastapi import Depends, HTTPException, status  # pip install fastapi
from fastapi.security import OAuth2PasswordBearer
from logging import getLogger
from src.core.config import settings

logger = getLogger(__name__)

# OAuth2PasswordBearer pour les endpoints sécurisés
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
  """
  Génère un token JWT pour l'authentification.

  Args:
    data (dict): Données à inclure dans le token.
    expires_delta (Optional[timedelta]): Durée de validité du token.

  Returns:
    str: Token JWT signé.
  """
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + \
      (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(
      to_encode,
      settings.SECRET_KEY,
      algorithm=settings.ALGORITHM
  )
  return encoded_jwt


def verify_access_token(token: str) -> dict:
  """
  Vérifie et décode un token JWT.

  Args:
      token (str): Token JWT à vérifier.

  Returns:
      dict: Données décodées du token.

  Raises:
      HTTPException: Si le token est invalide ou expiré.
  """
  try:
    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )
    return payload
  except JWTError as e:
    logger.error(f"Erreur de validation du token : {e}")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalide ou expiré",
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
  """
  Dépendance pour récupérer l'utilisateur actuel à partir du token.

  Args:
      token (str): Token JWT fourni par l'utilisateur.

  Returns:
      dict: Données de l'utilisateur.
  """
  payload = verify_access_token(token)
  return payload

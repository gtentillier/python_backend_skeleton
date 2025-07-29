from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from logging import getLogger
from src.core.security import get_current_user
from src.core.config import settings
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.models.user import User

logger = getLogger(__name__)
router = APIRouter(prefix="/users", tags=["users"])

# --- Endpoints ---

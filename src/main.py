"""Main entrypoint for FastAPI application.

This file configures the FastAPI app, includes routers, and sets up logging.
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.users import router as users_router
from src.core.config import settings


def configure_logging() -> None:
  """Configure logging for the application."""
  logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s %(levelname)s %(name)s %(message)s",
  )
  logger = logging.getLogger(__name__)
  logger.info("Logging is configured.")


def create_app() -> FastAPI:
  """Create and configure FastAPI app.

  Returns:
      FastAPI: The configured FastAPI application.
  """
  app = FastAPI(
      title="Projet Full‑Stack API",
      version="1.0.0",
      docs_url="/docs",
      redoc_url="/redoc",
  )

  # CORS configuration
  app.add_middleware(
      CORSMiddleware,
      allow_origins=settings.CORS_ORIGINS,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )

  # Routers
  app.include_router(users_router)

  return app


# Entrypoint
configure_logging()
app = create_app()

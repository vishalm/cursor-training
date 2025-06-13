import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import cart_routes
import logging
from logging.handlers import RotatingFileHandler
import os

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Food Order Cart API",
        description="API for managing food order carts with AI capabilities",
        version=settings.API_VERSION,
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Setup logging
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    handler = RotatingFileHandler(
        settings.LOG_FILE,
        maxBytes=10000000,  # 10MB
        backupCount=5
    )
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    
    logger = logging.getLogger("app")
    logger.setLevel(settings.LOG_LEVEL)
    logger.addHandler(handler)

    # Include routers
    app.include_router(
        cart_routes.router,
        prefix=f"{settings.API_PREFIX}/{settings.API_VERSION}",
        tags=["cart"]
    )

    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy"}

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.FLASK_DEBUG
    ) 
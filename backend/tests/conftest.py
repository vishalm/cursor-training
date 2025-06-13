import pytest
import os
from datetime import datetime, timedelta
from app.core.config import Settings
from app.services.cart_service import CartService

@pytest.fixture(scope="session")
def test_settings():
    """Test settings fixture."""
    return Settings(
        FLASK_APP="run.py",
        FLASK_ENV="test",
        FLASK_DEBUG=True,
        API_VERSION="v1",
        API_PREFIX="/api",
        OLLAMA_BASE_URL="http://localhost:11434",
        OLLAMA_MODEL="qwen2.5:latest",
        OLLAMA_TEMPERATURE=0.7,
        OLLAMA_MAX_TOKENS=1000,
        OLLAMA_TIMEOUT=30,
        STORAGE_TYPE="memory",
        STORAGE_CLEANUP_INTERVAL=3600,
        MAX_CART_ITEMS=50,
        MAX_CONVERSATION_AGE=86400,
        JWT_SECRET="test_secret",
        JWT_ALGORITHM="HS256",
        JWT_EXPIRATION=3600
    )

@pytest.fixture(scope="function")
def cart_service():
    """Cart service fixture."""
    service = CartService()
    yield service
    # Cleanup after each test
    service._carts.clear()

@pytest.fixture
def sample_cart():
    """Sample cart fixture."""
    return {
        "conversation_id": "test123",
        "items": [
            {
                "item_id": "item1",
                "quantity": 2,
                "special_instructions": "Extra spicy",
                "modifiers": [
                    {"id": "mod1", "quantity": 1},
                    {"id": "mod2", "quantity": 2}
                ]
            }
        ],
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

@pytest.fixture
def expired_cart():
    """Expired cart fixture."""
    return {
        "conversation_id": "expired123",
        "items": [
            {
                "item_id": "item1",
                "quantity": 1,
                "special_instructions": "Normal",
                "modifiers": []
            }
        ],
        "created_at": datetime.now() - timedelta(days=2),
        "updated_at": datetime.now() - timedelta(days=2)
    }

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment."""
    # Set test environment variables
    os.environ["FLASK_ENV"] = "test"
    os.environ["FLASK_DEBUG"] = "1"
    
    yield
    
    # Cleanup after all tests
    if "FLASK_ENV" in os.environ:
        del os.environ["FLASK_ENV"]
    if "FLASK_DEBUG" in os.environ:
        del os.environ["FLASK_DEBUG"] 
import pytest
from fastapi.testclient import TestClient
from app.models.cart_models import CartItem, Modifier
from run import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_cart_item():
    return {
        "item_id": "item1",
        "quantity": 2,
        "special_instructions": "Extra spicy",
        "modifiers": [
            {"id": "mod1", "quantity": 1},
            {"id": "mod2", "quantity": 2}
        ]
    }

def test_create_and_get_cart(client, sample_cart_item):
    conversation_id = "test123"
    
    # Add item to cart
    response = client.post(f"/api/v1/cart/{conversation_id}/items", json=sample_cart_item)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["items"]) == 1
    assert data["items"][0]["item_id"] == sample_cart_item["item_id"]
    
    # Get cart
    response = client.get(f"/api/v1/cart/{conversation_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["items"]) == 1
    assert data["items"][0]["item_id"] == sample_cart_item["item_id"]

def test_get_nonexistent_cart(client):
    response = client.get("/api/v1/cart/nonexistent")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert "error" in data

def test_update_cart_item(client, sample_cart_item):
    conversation_id = "test123"
    
    # Add item
    client.post(f"/api/v1/cart/{conversation_id}/items", json=sample_cart_item)
    
    # Update item
    updated_item = sample_cart_item.copy()
    updated_item["quantity"] = 3
    updated_item["special_instructions"] = "Less spicy"
    
    response = client.put(
        f"/api/v1/cart/{conversation_id}/items/{sample_cart_item['item_id']}",
        json=updated_item
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["items"]) == 1
    assert data["items"][0]["quantity"] == 3
    assert data["items"][0]["special_instructions"] == "Less spicy"

def test_update_nonexistent_item(client, sample_cart_item):
    conversation_id = "test123"
    response = client.put(
        f"/api/v1/cart/{conversation_id}/items/nonexistent",
        json=sample_cart_item
    )
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert "error" in data

def test_delete_cart_item(client, sample_cart_item):
    conversation_id = "test123"
    
    # Add item
    client.post(f"/api/v1/cart/{conversation_id}/items", json=sample_cart_item)
    
    # Delete item
    response = client.delete(
        f"/api/v1/cart/{conversation_id}/items/{sample_cart_item['item_id']}"
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["items"]) == 0

def test_delete_nonexistent_item(client):
    conversation_id = "test123"
    response = client.delete(f"/api/v1/cart/{conversation_id}/items/nonexistent")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert "error" in data

def test_place_order(client, sample_cart_item):
    conversation_id = "test123"
    
    # Add item
    client.post(f"/api/v1/cart/{conversation_id}/items", json=sample_cart_item)
    
    # Place order
    response = client.post(f"/api/v1/cart/{conversation_id}/order")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["items"]) == 1

def test_place_order_empty_cart(client):
    conversation_id = "test123"
    response = client.post(f"/api/v1/cart/{conversation_id}/order")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert "error" in data

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy" 
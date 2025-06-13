import pytest
from datetime import datetime, timedelta
from app.services.cart_service import CartService
from app.models.cart_models import Cart, CartItem, Modifier

@pytest.fixture
def cart_service():
    return CartService()

@pytest.fixture
def sample_cart_item():
    return CartItem(
        item_id="item1",
        quantity=2,
        special_instructions="Extra spicy",
        modifiers=[
            Modifier(id="mod1", quantity=1),
            Modifier(id="mod2", quantity=2)
        ]
    )

def test_create_cart(cart_service):
    conversation_id = "test123"
    cart = cart_service.create_cart(conversation_id)
    
    assert cart.conversation_id == conversation_id
    assert len(cart.items) == 0
    assert isinstance(cart.created_at, datetime)
    assert isinstance(cart.updated_at, datetime)

def test_create_duplicate_cart(cart_service):
    conversation_id = "test123"
    cart_service.create_cart(conversation_id)
    
    with pytest.raises(ValueError, match="Cart already exists"):
        cart_service.create_cart(conversation_id)

def test_get_cart(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart = cart_service.create_cart(conversation_id)
    cart_service.add_item(conversation_id, sample_cart_item)
    
    retrieved_cart = cart_service.get_cart(conversation_id)
    assert retrieved_cart.conversation_id == conversation_id
    assert len(retrieved_cart.items) == 1
    assert retrieved_cart.items[0].item_id == sample_cart_item.item_id

def test_get_nonexistent_cart(cart_service):
    assert cart_service.get_cart("nonexistent") is None

def test_add_item(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart = cart_service.add_item(conversation_id, sample_cart_item)
    
    assert len(cart.items) == 1
    assert cart.items[0].item_id == sample_cart_item.item_id
    assert cart.items[0].quantity == sample_cart_item.quantity
    assert cart.items[0].special_instructions == sample_cart_item.special_instructions
    assert len(cart.items[0].modifiers) == len(sample_cart_item.modifiers)

def test_update_item(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart = cart_service.add_item(conversation_id, sample_cart_item)
    
    updated_item = CartItem(
        item_id="item1",
        quantity=3,
        special_instructions="Less spicy",
        modifiers=[Modifier(id="mod1", quantity=2)]
    )
    
    updated_cart = cart_service.update_item(conversation_id, "item1", updated_item)
    assert len(updated_cart.items) == 1
    assert updated_cart.items[0].quantity == 3
    assert updated_cart.items[0].special_instructions == "Less spicy"
    assert len(updated_cart.items[0].modifiers) == 1

def test_update_nonexistent_item(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart_service.add_item(conversation_id, sample_cart_item)
    
    with pytest.raises(ValueError, match="Item not found"):
        cart_service.update_item(conversation_id, "nonexistent", sample_cart_item)

def test_remove_item(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart = cart_service.add_item(conversation_id, sample_cart_item)
    
    updated_cart = cart_service.remove_item(conversation_id, "item1")
    assert len(updated_cart.items) == 0

def test_remove_nonexistent_item(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart_service.add_item(conversation_id, sample_cart_item)
    
    with pytest.raises(ValueError, match="Item not found"):
        cart_service.remove_item(conversation_id, "nonexistent")

def test_clear_cart(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart = cart_service.add_item(conversation_id, sample_cart_item)
    
    cleared_cart = cart_service.clear_cart(conversation_id)
    assert len(cleared_cart.items) == 0

def test_cleanup_old_carts(cart_service, sample_cart_item):
    conversation_id = "test123"
    cart = cart_service.add_item(conversation_id, sample_cart_item)
    
    # Set cart's created_at to be older than MAX_CONVERSATION_AGE
    cart.created_at = datetime.utcnow() - timedelta(days=2)
    
    cart_service.cleanup_old_carts()
    assert cart_service.get_cart(conversation_id) is None 
from datetime import datetime
from typing import Dict, List, Optional
from ..models.cart_models import Cart, CartItem, CartResponse, ErrorResponse
from ..core.config import settings

class CartService:
    def __init__(self):
        self._carts: Dict[str, Cart] = {}

    def get_cart(self, conversation_id: str) -> Optional[Cart]:
        """Get a cart by conversation ID."""
        return self._carts.get(conversation_id)

    def create_cart(self, conversation_id: str) -> Cart:
        """Create a new cart."""
        if conversation_id in self._carts:
            raise ValueError("Cart already exists for this conversation")
        
        cart = Cart(conversation_id=conversation_id)
        self._carts[conversation_id] = cart
        return cart

    def add_item(self, conversation_id: str, item: CartItem) -> Cart:
        """Add an item to the cart."""
        cart = self.get_cart(conversation_id)
        if not cart:
            cart = self.create_cart(conversation_id)
        
        cart.items.append(item)
        cart.updated_at = datetime.utcnow()
        return cart

    def update_item(self, conversation_id: str, item_id: str, item: CartItem) -> Cart:
        """Update an item in the cart."""
        cart = self.get_cart(conversation_id)
        if not cart:
            raise ValueError("Cart not found")

        for i, existing_item in enumerate(cart.items):
            if existing_item.item_id == item_id:
                cart.items[i] = item
                cart.updated_at = datetime.utcnow()
                return cart
        
        raise ValueError("Item not found in cart")

    def remove_item(self, conversation_id: str, item_id: str) -> Cart:
        """Remove an item from the cart."""
        cart = self.get_cart(conversation_id)
        if not cart:
            raise ValueError("Cart not found")

        cart.items = [item for item in cart.items if item.item_id != item_id]
        cart.updated_at = datetime.utcnow()
        return cart

    def clear_cart(self, conversation_id: str) -> Cart:
        """Clear all items from the cart."""
        cart = self.get_cart(conversation_id)
        if not cart:
            raise ValueError("Cart not found")

        cart.items = []
        cart.updated_at = datetime.utcnow()
        return cart

    def get_cart_response(self, cart: Cart) -> CartResponse:
        """Convert a Cart to a CartResponse."""
        return CartResponse(
            success=True,
            conversation_id=cart.conversation_id,
            items=cart.items,
            total_items=len(cart.items),
            created_at=cart.created_at,
            updated_at=cart.updated_at
        )

    def cleanup_old_carts(self) -> None:
        """Remove carts older than MAX_CONVERSATION_AGE."""
        current_time = datetime.utcnow()
        self._carts = {
            conv_id: cart
            for conv_id, cart in self._carts.items()
            if (current_time - cart.updated_at).total_seconds() < settings.MAX_CONVERSATION_AGE
        }

cart_service = CartService() 
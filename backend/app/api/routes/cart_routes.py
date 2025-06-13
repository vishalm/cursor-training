from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.models.cart_models import (
    Cart,
    CartItem,
    CartResponse,
    ErrorResponse,
    Modifier
)
from app.services.cart_service import CartService
from app.services.ai_service import AIService

router = APIRouter(prefix="/cart")
cart_service = CartService()
ai_service = AIService()

@router.get(
    "/{conversation_id}",
    response_model=CartResponse,
    responses={404: {"model": ErrorResponse}}
)
async def get_cart(conversation_id: str):
    """Get all items in a cart."""
    try:
        cart = cart_service.get_cart(conversation_id)
        if not cart:
            raise HTTPException(
                status_code=404,
                detail=f"Cart not found for conversation ID: {conversation_id}"
            )
        return cart_service.get_cart_response(cart)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/{conversation_id}/items",
    response_model=CartResponse,
    responses={400: {"model": ErrorResponse}}
)
async def add_item(
    conversation_id: str,
    item: CartItem
):
    """Add an item to the cart."""
    try:
        # Process special instructions with AI if present
        if item.special_instructions:
            processed_instructions = await ai_service.process_cart_instructions(
                item.special_instructions
            )
            # You might want to update the item with processed instructions
            # or store them separately
        
        cart = cart_service.add_item(conversation_id, item)
        return cart_service.get_cart_response(cart)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/{conversation_id}/items/{item_id}",
    response_model=CartResponse,
    responses={404: {"model": ErrorResponse}}
)
async def get_item(conversation_id: str, item_id: str):
    """Get a specific item from the cart."""
    try:
        cart = cart_service.get_cart(conversation_id)
        if not cart:
            raise HTTPException(
                status_code=404,
                detail=f"Cart not found for conversation ID: {conversation_id}"
            )
        
        item = next((i for i in cart.items if i.item_id == item_id), None)
        if not item:
            raise HTTPException(
                status_code=404,
                detail=f"Item not found in cart: {item_id}"
            )
        
        return cart_service.get_cart_response(cart)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put(
    "/{conversation_id}/items/{item_id}",
    response_model=CartResponse,
    responses={404: {"model": ErrorResponse}}
)
async def update_item(
    conversation_id: str,
    item_id: str,
    item: CartItem
):
    """Update a specific item in the cart."""
    try:
        cart = cart_service.update_item(conversation_id, item_id, item)
        return cart_service.get_cart_response(cart)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete(
    "/{conversation_id}/items/{item_id}",
    response_model=CartResponse,
    responses={404: {"model": ErrorResponse}}
)
async def delete_item(conversation_id: str, item_id: str):
    """Delete a specific item from the cart."""
    try:
        cart = cart_service.remove_item(conversation_id, item_id)
        return cart_service.get_cart_response(cart)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/{conversation_id}/order",
    response_model=CartResponse,
    responses={404: {"model": ErrorResponse}}
)
async def place_order(conversation_id: str):
    """Place an order from the cart."""
    try:
        cart = cart_service.get_cart(conversation_id)
        if not cart:
            raise HTTPException(
                status_code=404,
                detail=f"Cart not found for conversation ID: {conversation_id}"
            )
        
        # Generate order summary using AI
        order_summary = await ai_service.summarize_order(cart)
        
        # You might want to store the order in a database here
        
        return cart_service.get_cart_response(cart)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
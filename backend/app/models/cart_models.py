from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator

class Modifier(BaseModel):
    id: str = Field(..., description="Unique identifier for the modifier")
    quantity: int = Field(..., ge=1, le=10, description="Quantity of the modifier")

class CartItem(BaseModel):
    item_id: str = Field(..., description="Unique identifier for the menu item")
    quantity: int = Field(..., ge=1, le=12, description="Quantity of the item")
    instructions: Optional[str] = Field(None, max_length=500, description="Special instructions for the item")
    modifiers: Optional[List[Modifier]] = Field(default=[], description="List of item modifiers")

    @validator('modifiers')
    def validate_modifiers(cls, v):
        if v is None:
            return []
        if len(v) > 10:
            raise ValueError("Maximum 10 modifiers allowed per item")
        return v

class Cart(BaseModel):
    conversation_id: str = Field(..., description="Unique identifier for the conversation")
    items: List[CartItem] = Field(default=[], description="List of items in the cart")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('items')
    def validate_items(cls, v):
        if len(v) > 50:  # Maximum 50 items per cart
            raise ValueError("Maximum 50 items allowed in cart")
        return v

class CartResponse(BaseModel):
    success: bool = True
    conversation_id: str
    items: List[CartItem]
    total_items: int
    created_at: datetime
    updated_at: datetime

class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    code: str 
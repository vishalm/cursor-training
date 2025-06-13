import aiohttp
import json
from typing import List, Dict, Any
from app.core.config import settings
from app.models.cart_models import Cart

class AIService:
    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.OLLAMA_MODEL
        self.temperature = settings.OLLAMA_TEMPERATURE
        self.max_tokens = settings.OLLAMA_MAX_TOKENS
        self.timeout = settings.OLLAMA_TIMEOUT

    async def _make_request(self, prompt: str) -> Dict[str, Any]:
        """Make a request to the Ollama API."""
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "temperature": self.temperature,
                        "max_tokens": self.max_tokens
                    },
                    timeout=self.timeout
                ) as response:
                    if response.status != 200:
                        raise Exception(f"Ollama API error: {response.status}")
                    
                    result = await response.json()
                    return json.loads(result.get("response", "{}"))
            except aiohttp.ClientError as e:
                raise Exception(f"Error connecting to Ollama API: {str(e)}")
            except json.JSONDecodeError as e:
                raise Exception(f"Error parsing Ollama API response: {str(e)}")

    async def process_cart_instructions(self, instructions: str) -> Dict[str, Any]:
        """Process food order instructions to extract key information."""
        prompt = f"""
        Analyze the following food order instructions and extract key information:
        {instructions}
        
        Return a JSON object with the following structure:
        {{
            "spice_level": "mild/medium/hot",
            "allergies": ["list", "of", "allergies"],
            "preferences": ["list", "of", "preferences"],
            "special_requests": ["list", "of", "special", "requests"]
        }}
        """
        return await self._make_request(prompt)

    async def suggest_items(self, cart_items: List[Dict[str, Any]], preferences: List[str]) -> List[str]:
        """Suggest additional items based on current cart items and preferences."""
        prompt = f"""
        Based on the current cart items:
        {json.dumps(cart_items, indent=2)}
        
        And user preferences:
        {json.dumps(preferences, indent=2)}
        
        Suggest additional items that would complement the order.
        Return a JSON array of item IDs.
        """
        return await self._make_request(prompt)

    async def summarize_order(self, cart: Cart) -> str:
        """Generate a natural language summary of the order."""
        prompt = f"""
        Create a natural language summary of the following food order:
        {json.dumps(cart.dict(), indent=2)}
        
        Focus on:
        1. Total number of items
        2. Special instructions
        3. Notable combinations
        4. Any dietary considerations
        """
        return await self._make_request(prompt)

ai_service = AIService() 
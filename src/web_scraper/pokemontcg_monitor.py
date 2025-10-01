import httpx
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.pokemontcg.io/v2/cards"
API_KEY = os.getenv("POKEMON_TCG_API")

HEADERS = {
    "X-Api-Key": API_KEY
}

async def fetch_cards(card_id: str = "xy1-1") -> dict:
    """Fetch a card by ID from the Pokémon TCG API."""
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
        params = {"q": f"id:{card_id}"}
        response = await client.get(API_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        return data


async def main():
    data = await fetch_cards("xy1-1")
    print(data)  


if __name__ == "__main__":
    asyncio.run(main())

import pytest
import httpx
import respx

from src.web_scraper.pokemontcg_monitor import fetch_cards, API_URL, HEADERS

@pytest.mark.asyncio
@respx.mock
async def test_fetch_cards_returns_expected_data():
    card_id = "xy1-1"
    mock_data = {
        "data": [{
            "id": card_id,
            "name": "Venusaur-EX",
            "set": {"name": "XY Base Set"}
        }]
    }
    respx.get(API_URL).mock(return_value=httpx.Response(200, json=mock_data))
    result = await fetch_cards(card_id)
    assert "data" in result
    assert result["data"][0]["id"] == card_id
    assert result["data"][0]["name"] == "Venusaur-EX"

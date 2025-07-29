from fastapi import APIRouter, Query
import httpx

router = APIRouter()

@router.get("/binance/price", tags=["Binance"])
async def get_binance_price(symbol: str = Query(..., description="Пара, например BTCUSDT")):
    """
    Получить текущую цену символа на Binance (например, BTCUSDT)
    """
    url = f"https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol.upper()}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code != 200:
            return {"error": "Unable to fetch data from Binance"}
        data = response.json()
    return {"symbol": data["symbol"], "price": data["price"]}

from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/binance/symbols", tags=["Binance"])
async def get_binance_symbols():
    """
    Получить список всех торговых пар на Binance
    """
    url = "https://api.binance.com/api/v3/exchangeInfo"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()
        symbols = [item["symbol"] for item in data["symbols"]]
    return {"symbols": symbols}


from fastapi import APIRouter, Query
import httpx

router = APIRouter()

@router.get("/binance/orderbook", tags=["Binance"])
async def get_binance_orderbook(symbol: str = Query(...), limit: int = 5):
    """
    Получить стакан ордеров (order book) для выбранной пары
    """
    url = "https://api.binance.com/api/v3/depth"
    params = {"symbol": symbol.upper(), "limit": limit}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        data = resp.json()
    return data
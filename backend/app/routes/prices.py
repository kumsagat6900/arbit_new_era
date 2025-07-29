from fastapi import APIRouter, Query
import httpx

router = APIRouter()

@router.get("/prices", tags=["Арбитраж"])
async def get_prices(symbol: str = Query("BTCUSDT")):
    async with httpx.AsyncClient() as client:
        binance = await client.get("https://api.binance.com/api/v3/ticker/price", params={"symbol": symbol})
        bybit = await client.get("https://api.bybit.com/v5/market/tickers", params={"category": "spot", "symbol": symbol})
        binance_price = binance.json().get("price")
        bybit_result = bybit.json()["result"]["list"]
        bybit_price = bybit_result[0]["lastPrice"] if bybit_result else None
    return {
        "symbol": symbol,
        "binance": binance_price,
        "bybit": bybit_price
    }
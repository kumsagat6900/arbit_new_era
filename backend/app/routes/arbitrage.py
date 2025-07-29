from fastapi import APIRouter, Query
import httpx

router = APIRouter()

@router.get("/arbitrage", tags=["Арбитраж"])
async def arbitrage_opportunity(symbol: str = Query("BTCUSDT")):
    async with httpx.AsyncClient() as client:
        binance = await client.get("https://api.binance.com/api/v3/ticker/price", params={"symbol": symbol})
        bybit = await client.get("https://api.bybit.com/v5/market/tickers", params={"category": "spot", "symbol": symbol})
        binance_price = float(binance.json().get("price", 0))
        bybit_result = bybit.json()["result"]["list"]
        bybit_price = float(bybit_result[0]["lastPrice"]) if bybit_result else 0
        diff = round(bybit_price - binance_price, 4)
    return {
        "symbol": symbol,
        "binance": binance_price,
        "bybit": bybit_price,
        "difference": diff
    }
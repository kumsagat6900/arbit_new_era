from fastapi import APIRouter

router = APIRouter()

@router.get("/exchanges", tags=["Биржи"])
async def get_exchanges():
    """
    Получить список поддерживаемых бирж
    """
    return {
        "exchanges": [
            {"name": "Binance", "url": "https://binance.com"},
            {"name": "Bybit", "url": "https://bybit.com"},
            {"name": "KuCoin", "url": "https://kucoin.com"},
            {"name": "OKX", "url": "https://okx.com"},
        ]
    }
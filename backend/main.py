from fastapi import FastAPI
from app.routes.exchanges import router as exchanges_router
from app.routes.binance import router as binance_router
from app.routes.prices import router as prices_router
from app.routes.arbitrage import router as arbitrage_router

app = FastAPI(title="Arbitrage Backend")

app.include_router(exchanges_router)
app.include_router(binance_router)
app.include_router(prices_router)
app.include_router(arbitrage_router)

@app.get("/")
async def root():
    return {"message": "Arbitrage backend is running"}
from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(title="Mini Production Platform API")

app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "service": "api",
        "message": "Mini Production Platform API is running"
    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import alerts

app = FastAPI(
    title="AvtoDozor API",
    version="1.0.0",
    description="Backend for AvtoDozor mobile app"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])

@app.get("/")
async def root():
    return {"message": "AvtoDozor API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}
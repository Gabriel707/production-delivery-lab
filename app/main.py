from fastapi import FastAPI, status

from app.api.routes import health, patients


app = FastAPI(title="Emergency Flow API")


app.include_router(health.router)
app.include_router(patients.router)
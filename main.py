from fastapi import FastAPI
from db import get_connection

app = FastAPI(title="Emergency Flow API")


@app.get("/")
def root():
    return {"message": "Emergency Flow API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/patients")
def list_patients():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, status, created_at FROM patients ORDER BY id;"
            )

            patients = cur.fetchall()

    return {
        "patients": [
            {
                "id": patient[0],
                "name": patient[1],
                "status": patient[2],
                "created_at": patient[3],
            }
            for patient in patients
        ]
    }
        
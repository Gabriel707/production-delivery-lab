from fastapi import FastAPI

app = FastAPI(title="Emergency Flow API")


@app.get("/")
def root():
    return {"message": "Emergency Flow API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/patients")
def list_patients():
    return {
        "patients": [
            {"id": 1, "name": "Jose Teste", "status": "waiting"}
        ]
    }
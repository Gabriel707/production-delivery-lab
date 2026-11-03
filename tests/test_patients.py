from fastapi.testclient import TestClient

from app.main import app
from app.api.routes import patients as patient_routes


client = TestClient(app)


def test_list_patients(monkeypatch):
    fake_patients = [
        {
            "id": 1,
            "name": "Maria Demo",
            "status": "waiting",
            "created_at": "2026-11-03T10:00:00",
        },
        {
            "id": 2,
            "name": "Carlos Demo",
            "status": "in_progress",
            "created_at": "2026-11-03T10:30:00",
        },
    ]

    def mock_list_patients():
        return fake_patients

    monkeypatch.setattr(
        patient_routes.patient_service,
        "list_patients",
        mock_list_patients,
    )

    response = client.get("/patients")

    assert response.status_code == 200
    assert response.json() == fake_patients


def test_create_patient(monkeypatch):
    fake_patient = {
        "id": 3,
        "name": "Dudubi Demo",
        "status": "waiting",
        "created_at": "2026-11-03T11:00:00",
    }

    def mock_create_patient(name, status):
        return fake_patient

    monkeypatch.setattr(
        patient_routes.patient_service,
        "create_patient",
        mock_create_patient,
    )

    response = client.post(
        "/patients",
        json={
            "name": "Beatriz Demo",
            "status": "waiting",
        },
    )

    assert response.status_code == 201
    assert response.json() == fake_patient


def test_create_patient_without_name():
    response = client.post(
        "/patients",
        json={
            "status": "waiting",
        },
    )

    assert response.status_code == 422

    response_data = response.json()

    assert response_data["detail"][0]["loc"] == ["body", "name"]
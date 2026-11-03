from app.repositories import patients as patient_repository


def list_patients():
    return patient_repository.list_patients()


def create_patient(name: str, status: str):
    normalized_name = name.strip()
    normalized_status = status.strip().lower()

    return patient_repository.create_patient(
        name=normalized_name,
        status=normalized_status,
    )
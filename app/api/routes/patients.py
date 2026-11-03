from fastapi import APIRouter, status

from app.schemas.patients import PatientCreate, PatientResponse
from app.services import patients as patient_service


router = APIRouter(
    prefix="/patients",
    tags=["patients"],
)


@router.get("", response_model=list[PatientResponse])
def list_patients():
    return patient_service.list_patients()


@router.post(
    "",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_patient(patient: PatientCreate):
    return patient_service.create_patient(
        name=patient.name,
        status=patient.status,
    )
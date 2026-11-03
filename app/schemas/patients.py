from datetime import datetime

from pydantic import BaseModel, Field


class PatientCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    status: str = Field(min_length=2, max_length=30)


class PatientResponse(BaseModel):
    id: int
    name: str
    status: str
    created_at: datetime
from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/")
def root():
    return {"message": "Emergency Flow API is up and running"}


@router.get("/health")
def health():
    return {"status": "ok"}
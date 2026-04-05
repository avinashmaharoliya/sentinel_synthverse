from fastapi import APIRouter
from services.analytics import get_stats

router = APIRouter()

def init(patients_data):
    global patients
    patients = patients_data

@router.get("/")
def stats():
    return get_stats(patients)
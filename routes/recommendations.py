from fastapi import APIRouter
from services.recommendation import recommend_antibiotic

router = APIRouter()

def init(patients_data, resistance_data):
    global patients, resistance_map
    patients = patients_data
    resistance_map = resistance_data

@router.get("/{pid}")
def get_recommendation(pid: int):
    patient = patients.get(pid)

    if not patient:
        return {"error": "Patient not found"}

    drug = recommend_antibiotic(patient, resistance_map)

    return {"recommended": drug}
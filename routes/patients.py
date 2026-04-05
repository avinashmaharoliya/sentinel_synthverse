from fastapi import APIRouter

router = APIRouter()

def init(patients_data):
    global patients
    patients = patients_data

@router.get("/")
def get_all_patients():
    return patients

@router.get("/{pid}")
def get_patient(pid: int):
    return patients.get(pid, {"error": "Patient not found"})
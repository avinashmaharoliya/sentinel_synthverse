from fastapi import APIRouter
from services.infection import spread_infection

router = APIRouter()

def init(patients_data, network_data):
    global patients, network
    patients = patients_data
    network = network_data

@router.post("/step")
def simulate():
    global patients
    patients = spread_infection(patients, network)
    return {"message": "Simulation step completed"}
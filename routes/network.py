from fastapi import APIRouter

router = APIRouter()

def init(network_data):
    global network
    network = network_data

@router.get("/")
def get_network():
    return network
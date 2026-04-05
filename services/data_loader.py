import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_data():
    data_path = os.path.join(BASE_DIR, "data")

    with open(os.path.join(data_path, "patients_clean.json")) as f:
        patients = json.load(f)

    with open(os.path.join(data_path, "network_clean.json")) as f:
        network = json.load(f)

    with open(os.path.join(data_path, "resistance_clean.json")) as f:
        resistance_raw = json.load(f)

    # Fix types
    patients = {int(k): v for k, v in patients.items()}
    network = {int(k): v for k, v in network.items()}

    resistance_map = {
        tuple(k.split("|")): v
        for k, v in resistance_raw.items()
    }

    return patients, network, resistance_map
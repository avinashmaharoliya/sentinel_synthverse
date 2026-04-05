from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.data_loader import load_data
from routes import patients, recommendations, stats, network ,simulation

app = FastAPI(title="ICU Digital Twin API")

# Enable CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data
patients_data, network_data, resistance_map = load_data()

# Initialize routes
patients.init(patients_data)
recommendations.init(patients_data, resistance_map)
stats.init(patients_data)
network.init(network_data)
simulation.init(patients_data, network_data)


# Register routes
app.include_router(patients.router, prefix="/patients")
app.include_router(recommendations.router, prefix="/recommend")
app.include_router(stats.router, prefix="/stats")
app.include_router(network.router, prefix="/network")
app.include_router(simulation.router, prefix="/simulate")   
@app.get("/")
def root():
    return {"message": "ICU Digital Twin API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
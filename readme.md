# 🧬 Sentinel: ICU Digital Twin & Infection Simulation System

> A full-stack digital twin platform for ICU monitoring, infection modeling, and treatment decision support.

---

## 📌 Overview

**Sentinel** is a Digital Twin ICU Simulation System that models an intensive care unit as a **connected biological network** rather than isolated patients.

It enables:
- Real-time patient monitoring  
- Infection spread simulation  
- Risk prediction  
- Treatment recommendation  
- Scenario-based decision testing  

---

## 🚨 Problem

ICU systems today are:
- Static dashboards  
- Reactive (not predictive)  
- Unable to model infection spread  
- Limited in decision support  

---

## 💡 Solution

Sentinel introduces a simulation-first architecture that:

- Represents ICU as a graph of patients  
- Simulates infection propagation  
- Provides treatment recommendations  
- Enables interactive intervention testing  

---

## 🧠 System Architecture

### High-Level Flow


Data → Backend Engine → Simulation → API → Frontend Visualization


---

## 🏗️ Backend Architecture (Python)

### Project Structure


backend/
│
├── data/
│ ├── network_clean.json
│ ├── patients_clean.json
│ └── resistance_clean.json
│
├── routes/
│ ├── network.py
│ ├── patients.py
│ ├── recommendations.py
│ ├── simulation.py
│ └── stats.py
│
├── services/
│ ├── analytics.py
│ ├── data_loader.py
│ ├── infection.py
│ └── recommendation.py
│
├── app.py
├── requirements.txt
└── Dockerfile


---

## ⚙️ Backend Responsibilities

### Data Layer
- Loads ICU data from JSON files  
- Maintains patient, network, and resistance datasets  

### Services Layer

- **infection.py** → Infection spread simulation  
- **recommendation.py** → Antibiotic suggestion logic  
- **analytics.py** → ICU metrics and insights  
- **data_loader.py** → Data parsing and normalization  

### API Layer

| Endpoint | Description |
|--------|------------|
| `/patients` | Fetch patient data |
| `/network` | Fetch ICU network |
| `/simulation` | Run infection simulation |
| `/recommendations` | Get treatment suggestions |
| `/stats` | Get ICU analytics |

---

## 💻 Frontend

- React-based dashboard  
- SVG network visualization  
- Simulation timeline (time travel)  
- Interactive controls  
- SITREP event console  

---

## ⚡ Key Features

### 🦠 Infection Simulation
- Predicts spread across ICU network  
- Identifies high-risk patients  

### 🌐 Network-Based ICU Model
- Patients = nodes  
- Connections = transmission paths  

### 💊 Treatment Support
- Suggests antibiotics based on resistance  
- Avoids ineffective treatments  

### ⏱️ Time Travel Simulation
- Replay ICU states  
- Analyze outbreak evolution  

### ⚡ Triage Override
- Manual intervention with instant recalculation  

---

## 🏗️ Tech Stack

### Backend
- Python  
- FastAPI / Flask  
- JSON-based data modeling  

### Frontend
- React 18  
- Vite  
- Tailwind CSS  
- Framer Motion  
- SVG + Recharts  

---

## 📦 Setup Instructions

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
Frontend
npm install
npm run dev
Docker (Optional)
docker build -t sentinel-backend .
docker run -p 5000:5000 sentinel-backend
🔮 Future Enhancements
WebSocket real-time updates
ML-based infection prediction
LLM-powered SITREP narratives
Hospital system integration (HL7/FHIR)
🧪 Use Cases
Healthcare simulations
Academic research
Hackathons
Training environments
Digital health prototypes
🧠 Key Insight

Sentinel transforms ICU monitoring from data viewing → system simulation → decision intelligence

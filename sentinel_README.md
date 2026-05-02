<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:0d0d0d,40:1a0533,100:0d1b2a&height=200&section=header&text=🛡️%20SENTINEL&fontSize=75&fontColor=c084fc&fontAlignY=45&desc=ICU%20Digital%20Twin%20%26%20Infection%20Simulation%20System&descSize=17&descColor=a78bfa&animation=fadeIn" width="100%"/>

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-Flask%2FFastAPI-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/React%2018-Vite-61DAFB?style=for-the-badge&logo=react&logoColor=black"/>
  <img src="https://img.shields.io/badge/Tailwind%20CSS-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Track-Digital%20Twins-c084fc?style=for-the-badge"/>
</p>

<br/>

> **🦠 Transforming ICU monitoring from reactive dashboards into predictive, simulation-driven intelligence.**

</div>

---

## 🧭 Table of Contents

- [What is Sentinel?](#-what-is-sentinel)
- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [Architecture](#️-architecture)
- [Key Features](#-key-features)
- [API Reference](#-api-reference)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Run](#-setup--run)
- [Future Enhancements](#-future-enhancements)

---

## 🌟 What is Sentinel?

**Sentinel** is a full-stack **ICU Digital Twin** platform that models an Intensive Care Unit as a **connected biological network** — not a collection of isolated patients. It enables:

```
Real-time monitoring  →  Infection simulation  →  Predictive risk scoring  →  Treatment decisions
```

> *A simulation-first approach to critical care intelligence.*

---

## 🚨 The Problem

Modern ICU systems are fundamentally broken in how they handle information:

| Current State | Why It Fails |
|:---|:---|
| 📊 Static dashboards | Only show current state — no prediction |
| 🔔 Reactive alerts | Respond *after* deterioration, not before |
| 🧍 Isolated patient views | Don't model cross-patient infection pathways |
| 💊 Manual treatment lookup | No intelligent antibiotic recommendation |
| 📂 Siloed data | No network-level insight into ICU dynamics |

---

## 💡 The Solution

Sentinel introduces a **simulation-first architecture** built on three principles:

```
① Model the ICU as a graph          — Patients = nodes, Transmission paths = edges
② Simulate before deciding          — Run infection spread models proactively
③ Recommend, don't just report      — Suggest treatments based on resistance data
```

---

## 🏗️ Architecture

```mermaid
flowchart TD
    subgraph DATA["📦 Data Layer"]
        A1[patients_clean.json]
        A2[network_clean.json]
        A3[resistance_clean.json]
    end

    subgraph SERVICES["⚙️ Services Layer"]
        B1[data_loader.py\nParsing & Normalization]
        B2[infection.py\nSpread Simulation]
        B3[recommendation.py\nAntibiotic Logic]
        B4[analytics.py\nICU Metrics]
    end

    subgraph API["🔌 API Layer (Flask/FastAPI)"]
        C1[/patients]
        C2[/network]
        C3[/simulation]
        C4[/recommendations]
        C5[/stats]
    end

    subgraph FRONTEND["💻 Frontend (React + Vite)"]
        D1[SVG Network Graph]
        D2[Simulation Timeline]
        D3[SITREP Console]
        D4[Intervention Controls]
    end

    DATA --> SERVICES
    SERVICES --> API
    API --> FRONTEND
```

---

## 🔑 Key Features

<table>
<tr>
<td width="50%">

### 🦠 Infection Simulation
- Graph-based spread modeling across ICU nodes
- Identifies highest-risk patients and transmission paths
- Replay and time-travel through outbreak evolution

</td>
<td width="50%">

### 🌐 Network-Based ICU Model
- Each patient = a node in a live infection graph
- Connections represent real transmission pathways
- Dynamic edge weighting based on proximity and contacts

</td>
</tr>
<tr>
<td width="50%">

### 💊 Treatment Decision Support
- Suggests antibiotics based on pathogen resistance profiles
- Eliminates ineffective treatments before they're prescribed
- Prioritizes interventions by urgency score

</td>
<td width="50%">

### ⏱️ Time Travel Simulation
- Scrub backward/forward through ICU state history
- Analyze counterfactual "what-if" interventions
- Instant recalculation on manual triage overrides

</td>
</tr>
</table>

---

## 🔌 API Reference

| Method | Endpoint | Description |
|:---:|:---|:---|
| `GET` | `/patients` | Fetch all patient records and vitals |
| `GET` | `/network` | Fetch ICU contact network graph |
| `POST` | `/simulation` | Trigger infection spread simulation |
| `GET` | `/recommendations` | Get treatment suggestions by patient |
| `GET` | `/stats` | Get aggregate ICU analytics |

---

## 🧰 Tech Stack

<div align="center">

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### Frontend
![React](https://img.shields.io/badge/React%2018-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind%20CSS-38B2AC?style=flat-square&logo=tailwindcss&logoColor=white)
![Framer Motion](https://img.shields.io/badge/Framer%20Motion-0055FF?style=flat-square&logo=framer&logoColor=white)
![Recharts](https://img.shields.io/badge/Recharts-SVG%20Viz-22d3ee?style=flat-square)

</div>

---

## 📁 Project Structure

```
sentinel_synthverse/
│
├── 📂 data/
│   ├── network_clean.json        # ICU patient network graph
│   ├── patients_clean.json       # Patient vitals & records
│   └── resistance_clean.json     # Pathogen resistance data
│
├── 📂 routes/
│   ├── network.py                # Network graph endpoints
│   ├── patients.py               # Patient data endpoints
│   ├── recommendations.py        # Treatment suggestion routes
│   ├── simulation.py             # Infection simulation trigger
│   └── stats.py                  # Analytics endpoints
│
├── 📂 services/
│   ├── analytics.py              # ICU metrics computation
│   ├── data_loader.py            # JSON parsing & normalization
│   ├── infection.py              # Graph-based spread model
│   └── recommendation.py        # Antibiotic decision logic
│
├── 📂 src/                       # React frontend source
├── 🖥️  app.py                    # Flask application entry
├── 🌐 index.html                 # Root HTML
├── 🐋 Dockerfile                 # Container config
├── 📦 requirements.txt           # Python dependencies
└── ⚙️  package.json              # Node dependencies
```

---

## 🚀 Setup & Run

### Backend

```bash
# Clone the repo
git clone https://github.com/avinashmaharoliya/sentinel_synthverse.git
cd sentinel_synthverse

# Set up virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start backend
python app.py
```

### Frontend

```bash
npm install
npm run dev
```

### Docker (Optional)

```bash
docker build -t sentinel-backend .
docker run -p 5000:5000 sentinel-backend
```

> Copy `.env.example` → `.env` and fill in required values before running.

---

## 🔮 Future Enhancements

- [ ] ⚡ WebSocket real-time patient monitoring
- [ ] 🤖 ML-based infection probability prediction
- [ ] 🧠 LLM-generated SITREP incident narratives
- [ ] 🏥 HL7/FHIR hospital system integration
- [ ] 📱 Mobile command dashboard for bedside use

---

## 🧪 Use Cases

```
🏥 Healthcare simulation training
🎓 Academic ICU modeling research
💡 Hackathon & digital health prototypes
🧪 Antibiotic stewardship decision support
```

---

## 📌 Note

> Sentinel is a **research and simulation prototype** built for the Synthverse 2026 hackathon. It is **not validated for clinical deployment**. Real patient data should never be used without proper anonymization and compliance frameworks.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:0d0d0d,40:1a0533,100:0d1b2a&height=80&section=footer" width="100%"/>

*From data viewing → system simulation → decision intelligence.*

</div>

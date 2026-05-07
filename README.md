# 🏭 Industrial IoT & OEE Monitoring Stack

A full-stack IIoT (Industrial Internet of Things) infrastructure for real-time industrial sensor data acquisition, database archiving, and automated OEE (Overall Equipment Effectiveness) metric calculation — visualized through a modern SCADA interface.

> [!IMPORTANT]
> The system is containerized on Docker using a modern microservices architecture and is designed in compliance with industrial OT (Operational Technology) standards.

---

## 🚀 Key Features

- 📡 **Real-time Data Acquisition:** Collects sensor data with millisecond latency over the MQTT protocol.
- 📊 **Automated OEE Calculation:** Instantly calculates Availability, Performance, and Quality metrics from production line data.
- 🗄️ **Database Persistence:** Stores all sensor data with timestamps in PostgreSQL as a time-series database.
- 🌉 **History Data Bridge:** Delivers historical data from the database to SCADA charts via a Node-RED based proxy.
- 🖥️ **Modern SCADA Interface:** Industrial-grade dashboard design built on the FUXA platform.

---

## 🏗️ System Architecture

The system consists of **5 integrated core layers**:

| Layer | Component | Description |
|-------|-----------|-------------|
| **Simulation Layer** | Node-RED | Simulates PLC/sensor data and publishes it over MQTT |
| **Messaging Layer** | Mosquitto MQTT | High-performance message broker handling inter-service communication |
| **Application Layer** | FastAPI / Python | Backend service for data processing, database persistence, and OEE analysis |
| **Storage Layer** | PostgreSQL | Relational database for secure and structured industrial data storage |
| **Visualization Layer** | FUXA SCADA | Visualization interface hosting operator and engineer dashboards |

---

## 🛠️ Tech Stack

| Component | Technology | Role |
|-----------|------------|------|
| Backend | Python 3.10+, FastAPI | Data processing and API management |
| Database | PostgreSQL | Time-series data storage |
| Messaging | MQTT (Mosquitto) | Device-to-device communication |
| Integration | Node-RED | Data flow management and proxy |
| Visualization | FUXA SCADA | Industrial dashboard |
| Infrastructure | Docker, Docker Compose | Containerization and orchestration |

---

## 📦 Getting Started

All you need is **Docker** and **Docker Compose** installed on your machine.

**1. Clone the repository:**

```bash
git clone https://github.com/username/industrial-oee-stack.git
cd industrial-oee-stack
```

**2. Start the Docker containers:**

```bash
docker compose up -d --build
```

**3. Access the interfaces:**

| Service | URL |
|---------|-----|
| 🌐 FUXA SCADA | http://localhost:1881 |
| 🔄 Node-RED | http://localhost:1880 |
| 🔌 FastAPI Docs | http://localhost:8000/docs |

---

## 📂 Project Structure

```
├── backend/
│   ├── app/
│   │   ├── api/          # OEE and History API routes
│   │   ├── core/         # DB connection and configuration
│   │   ├── services/     # MQTT listener and business logic
│   │   └── main.py       # Application entry point
│   └── Dockerfile
├── mosquitto/            # MQTT broker configuration
├── docker-compose.yml    # Full system orchestration
└── README.md
```

---

## 👨‍💻 Developer

**Ege Ertürk**  
Software Engineering Student

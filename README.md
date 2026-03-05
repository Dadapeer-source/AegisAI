# 🛡️ AegisAI – Autonomous Self-Healing System Monitor

AegisAI is an intelligent system monitoring platform designed to **detect system stress, predict risks, and automatically perform self-healing actions** to maintain system stability.

The system continuously monitors CPU, memory, disk usage, and running processes. Based on these metrics, it calculates risk levels and decides whether automated actions are required.

The project consists of three main components:

* **Agent** – collects system metrics
* **Brain** – analyzes data and makes decisions
* **UI** – visualizes system health in real time

---

# 📌 Project Architecture

```
AegisAI
│
├── aegisai-agent
│   System monitoring agent
│
├── aegisai-brain
│   Decision engine and API
│
└── aegisai-ui
    Dashboard interface
```

System workflow:

```
Agent → Collects system metrics
       ↓
Brain → Analyzes metrics and decides actions
       ↓
UI → Displays system health dashboard
```

---

# ⚙️ System Components

## 1. AegisAI Agent

The **Agent** is responsible for collecting system metrics such as:

* CPU usage
* Memory usage
* Disk usage
* Process information

The collected metrics are sent to the **Brain API** for analysis.

Features:

* Real-time system monitoring
* Lightweight background execution
* Process activity detection

**Developed by:** Dadapeer

---

## 2. AegisAI Brain

The **Brain** is the core intelligence of the system.

It performs the following tasks:

* Receives system metrics
* Calculates system risk
* Determines the required action
* Executes automated self-healing operations if necessary

Main modules include:

* Failure Predictor
* Decision Engine
* Automation Actions

The Brain API is built using **FastAPI** and runs using **Uvicorn**.

**Developed by:** Nanda Kumar P N

---

## 3. AegisAI Dashboard UI

The UI provides a real-time visualization of system health.

It displays:

* CPU usage
* Memory usage
* Disk usage
* Process count
* Risk level
* AI decision output

The frontend is built using:

* React
* Vite

**Developed by:** Navaneeth S

---

# 🧠 System Features

* Real-time system monitoring
* Risk prediction based on system metrics
* Automated self-healing mechanism
* Intelligent process management
* Interactive monitoring dashboard
* Modular system architecture

---

# 🚀 How the System Works

1. **Agent collects system data**

The agent monitors system resources such as CPU, memory, disk usage, and running processes.

2. **Data is processed by the Brain**

The Brain receives metrics and calculates system risk using the Failure Predictor.

3. **Decision engine evaluates the system**

The Decision Engine determines whether the system is in a safe or risky state.

4. **Self-healing actions are triggered**

If the system detects high stress conditions, it can automatically perform corrective actions.

5. **Dashboard displays the system state**

The UI fetches data from the Brain API and displays system health metrics.

---

# 🖥️ Requirements

Make sure the following software is installed:

* Python 3.11+
* Node.js
* npm

---

# ▶️ How to Run the Project

## 1️⃣ Run the Brain (Backend API)

Open terminal and navigate to the brain directory:

```
cd aegisai-brain
```

Install dependencies:

```
pip install -r requirements.txt
```

Start the API server:

```
python -m uvicorn api:app --reload
```

The backend will run at:

```
http://127.0.0.1:8000
```

Test the API using:

```
http://127.0.0.1:8000/docs
```

---

## 2️⃣ Run the Dashboard UI

Open another terminal and navigate to the UI folder:

```
cd aegisai-ui
```

Install dependencies:

```
npm install
```

Start the frontend server:

```
npm run dev
```

The dashboard will run at:

```
http://localhost:5173
```

---

## 3️⃣ Run the Agent

Open another terminal and start the monitoring agent:

```
cd aegisai-agent
python main.py
```

The agent will begin collecting system metrics.

---

# 📊 API Endpoint Example

System status can be retrieved from:

```
GET /status
```

Example response:

```
{
  "cpu": 14.6,
  "memory": 66.3,
  "disk": 40.7,
  "process_count": 312,
  "risk": "HIGH",
  "decision": "KILL_PROCESS"
}
```

---

# 📁 Project Structure

```
AegisAI
│
├── aegisai-agent
│   └── main.py
│
├── aegisai-brain
│   ├── api.py
│   ├── automation
│   └── logic
│
└── aegisai-ui
    ├── src
    └── components
```

---

# 👨‍💻 Team Contributions

| Component     | Responsibility                               | Developer       |
| ------------- | -------------------------------------------- | --------------- |
| AegisAI Agent | System monitoring and data collection        | Dadapeer        |
| AegisAI Brain | Risk prediction, decision engine, automation | Nanda Kumar P N |
| AegisAI UI    | Dashboard interface and visualization        | Navaneeth S     |

---

# 🔮 Future Improvements

Possible enhancements for future development:

* Advanced anomaly detection using machine learning
* Multi-system monitoring architecture
* Real-time event streaming
* Improved risk prediction models
* Enhanced automation strategies

---

# 📜 License

This project is developed for educational and research purposes.

# AegisAI Monitoring Agent (Member 1)

## Overview

This module is responsible for collecting real-time system and process-level data and storing it in a structured MySQL database for further analysis and machine learning.

---

## Features

* Collects CPU, Memory, Disk, Network usage
* Tracks top processes by CPU usage
* Stores data every 5 seconds
* Clean and structured dataset for ML models

---

## Database Details

### Database Name

aegisai_db

---

### Table 1: system_metrics

| Column           | Description          |
| ---------------- | -------------------- |
| timestamp        | Data collection time |
| cpu_usage        | CPU usage (%)        |
| memory_usage     | Memory usage (%)     |
| disk_usage       | Disk usage (%)       |
| network_sent     | Bytes sent           |
| network_received | Bytes received       |
| process_count    | Number of processes  |

---

### Table 2: process_metrics

| Column               | Description          |
| -------------------- | -------------------- |
| timestamp            | Data collection time |
| process_id           | Process ID           |
| process_name         | Process name         |
| process_cpu_usage    | CPU usage (%)        |
| process_memory_usage | Memory usage (%)     |
| execution_path       | Executable path      |
| parent_process       | Parent PID           |

---

## Data Frequency

Data is collected every 5 seconds.

---

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Start monitoring:
   python main.py

---

## Output

Data is continuously stored in MySQL and ready for:

* Machine Learning
* Anomaly Detection
* Dashboard Visualization

---

## Notes for Member 2

* Data is cleaned and filtered
* No null values
* Consistent timestamps
* Ready for ML training

# 🛰 Sentinel AI India v1 — Multi-Agent Command Centre

**The Unified Command Centre — where CloudShield X meets AutoPilot ML X**

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![asyncio](https://img.shields.io/badge/asyncio-Concurrency-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![pytest](https://img.shields.io/badge/pytest-5%20tests%20passing-brightgreen)
![Security](https://img.shields.io/badge/Security-Bandit%20Scanned-orange)

---

**Live Demo:** https://sentinel-ai-india-v1-hpqhmqzz2hevjgjeyfomka.streamlit.app/

---

## 🎯 What is Sentinel AI India?

Sentinel AI India is the **multi-agent brain** that unifies my two other flagship projects — [CloudShield X](https://github.com/dharunvishnu2006-ctrl/cloudshield-x-v1) (security) and [AutoPilot ML X](https://github.com/dharunvishnu2006-ctrl/autopilot-ml-x-v1) (machine learning) — into a single command centre.

v1 delivers the **agent backbone**: independent agents that communicate asynchronously, a priority-based task orchestrator, unified status reporting, and intelligent routing between agents.

---

## ✨ Features (v1 of 6)

- 🤖 **Agent Skeleton** — Independent agents with their own async message queues (OOP + `asyncio.Queue`)
- 📨 **Async Message Passing** — Agents communicate via `asyncio` without blocking each other
- ⚡ **Priority-Queue Orchestrator** — A min-heap (`heapq`) ensures the most urgent task is always served first
- 🌐 **Unified Flask API** — A single `/status` endpoint aggregates data from both CloudShield and AutoPilot
- 🗺 **Graph-based Agent Routing** — BFS finds the shortest communication path between any two agents

---

## 🧪 Results (from my own test run)

- ✅ 5/5 pytest tests passing
- ✅ Orchestrator correctly prioritized 3 tasks by urgency (Security Breach served before Routine Report)
- ✅ BFS routing found the correct 3-hop path: `CloudShield → Sentinel → AutoPilot`
- ✅ Unified API successfully aggregated live SQLite data from both flagships (CloudShield: 12 alerts, AutoPilot: 5 datasets)

---

## 🛠 How to Run Locally

```bash
git clone https://github.com/dharunvishnu2006-ctrl/sentinel-ai-india-v1.git
cd sentinel-ai-india-v1
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run app.py
```

---

## 🏗 Architecture

---

## 📚 What I Learned

- Designing multi-agent systems using OOP and independent message queues
- Using `asyncio` for concurrent, non-blocking communication between components
- Applying a min-heap (`heapq`) for real-time priority scheduling — O(log n) vs O(n log n) for repeated sorting
- Implementing BFS for guaranteed shortest-path graph traversal
- Building and testing a Flask API with SQLite-backed data aggregation
- Writing pytest tests for async code using `pytest-asyncio`
- Debugging real deployment issues — `.gitignore` excluding needed files, git submodule mix-ups, and cloud environment differences from local

---

## 🔗 Ecosystem

This project is part of a 3-flagship AI/ML + Cloud + Cyber Security portfolio:
- 🛡 [CloudShield X](https://github.com/dharunvishnu2006-ctrl/cloudshield-x-v1) — Security monitoring system
- 🚀 [AutoPilot ML X](https://github.com/dharunvishnu2006-ctrl/autopilot-ml-x-v1) — Automated ML pipeline
- 🛰 **Sentinel AI India** (this repo) — Unified command centre connecting both

**Roadmap:** v1 of 6 — growing toward a fully deployed, cloud-monitored multi-agent system.

---

## 👨‍💻 Author

**J. Dharun Vishnu**
BSc IT Student | Building toward AI/ML + Cloud + Cyber Security Engineering

---

## 🔒 Security

This code has been scanned with [Bandit](https://bandit.readthedocs.io/) for common security vulnerabilities.
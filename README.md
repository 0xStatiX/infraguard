# InfraGuard

**InfraGuard** is an intelligent, modular infrastructure monitoring system written in Python. It monitors server resources, tracks external services' availability, stores logs in a local database, and exposes a REST API for remote inspection and visualization.

## Features

- 🖥️ Monitor CPU, RAM, Disk, Network usage
- 🌐 Track uptime of external services
- 🧠 Intelligent threshold alerts (coming soon)
- 📦 FastAPI REST API
- 🗄️ SQLAlchemy + SQLite logging
- 📁 Modular, extensible plugin design

## Setup

```bash
pip install -r requirements.txt
uvicorn infraguard.api:app --reload
```

Then navigate to `http://localhost:8000/docs`

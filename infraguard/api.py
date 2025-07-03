from fastapi import FastAPI
from infraguard.core.monitor import get_system_metrics
from infraguard.core.network import check_services
from infraguard.db import log_metrics, get_last_metrics

app = FastAPI(title="InfraGuard")

@app.get("/metrics/system")
def system_metrics():
    data = get_system_metrics()
    log_metrics(data)
    return data

@app.get("/metrics/services")
def service_status():
    return check_services()

@app.get("/metrics/latest")
def last_metrics():
    return get_last_metrics()

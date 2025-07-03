import psutil
import platform
import datetime

def get_system_metrics():
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "platform": platform.system(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage("/")._asdict(),
        "net_io": psutil.net_io_counters()._asdict(),
    }

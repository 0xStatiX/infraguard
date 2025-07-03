from sqlalchemy import create_engine, Column, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
import json

Base = declarative_base()
engine = create_engine("sqlite:///infraguard/metrics.db")
Session = sessionmaker(bind=engine)
session = Session()

class Metric(Base):
    __tablename__ = "metrics"
    timestamp = Column(DateTime, primary_key=True)
    platform = Column(String)
    cpu_percent = Column(Float)
    memory = Column(JSON)
    disk = Column(JSON)
    net_io = Column(JSON)

Base.metadata.create_all(engine)

def log_metrics(data):
    metric = Metric(
        timestamp=datetime.fromisoformat(data["timestamp"]),
        platform=data["platform"],
        cpu_percent=data["cpu_percent"],
        memory=data["memory"],
        disk=data["disk"],
        net_io=data["net_io"]
    )
    session.add(metric)
    session.commit()

def get_last_metrics():
    last = session.query(Metric).order_by(Metric.timestamp.desc()).first()
    return {
        "timestamp": last.timestamp.isoformat(),
        "platform": last.platform,
        "cpu_percent": last.cpu_percent,
        "memory": json.loads(last.memory),
        "disk": json.loads(last.disk),
        "net_io": json.loads(last.net_io)
    } if last else {}

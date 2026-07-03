import json
from datetime import datetime

print("🔍 Real-Time Streaming Data Lineage...")

lineage = {
    "pipeline": "Real-Time Financial Streaming Platform",
    "created_at": datetime.now().isoformat(),
    "architecture": {
        "source": "Yahoo Finance API / Simulated Market Data",
        "ingestion": "Apache Kafka (Topic: financial-transactions)",
        "processing": "Apache Spark Structured Streaming",
        "storage": "Google BigQuery",
        "monitoring": "Kafka UI Dashboard"
    },
    "data_flow": [
        "Stock Market Data → Kafka Producer",
        "Kafka Producer → financial-transactions topic",
        "Spark Streaming → Consumes Kafka topic",
        "Spark → Aggregations (avg price, volume, change%)",
        "Spark → Google BigQuery (analytics layer)",
        "Kafka UI → Real-time monitoring"
    ],
    "stocks": ["AAPL", "MSFT", "GOOGL", "JPM", "BAC"],
    "metrics": {
        "throughput": "5 messages/2 seconds",
        "latency": "< 1 second",
        "processing": "Real-time aggregations every 10 seconds"
    }
}

print("\n📊 PIPELINE ARCHITECTURE:")
print("=" * 50)
for step in lineage["data_flow"]:
    print(f"  → {step}")

print(f"\n⚡ METRICS:")
for k, v in lineage["metrics"].items():
    print(f"  {k}: {v}")

with open("scripts/lineage_report.json", "w") as f:
    json.dump(lineage, f, indent=2)

print("\n✅ Lineage report saved!")
print("🎉 Real-Time Financial Streaming Platform - Complete!")

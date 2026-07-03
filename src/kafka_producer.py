import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer
import yfinance as yf

print("🚀 Starting Real-Time Financial Data Producer...")

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

STOCKS = ['AAPL', 'MSFT', 'GOOGL', 'JPM', 'BAC']
TOPIC = 'financial-transactions'

def generate_stock_data(symbol):
    """Generate real-time stock data"""
    base_prices = {
        'AAPL': 150.0, 'MSFT': 380.0, 
        'GOOGL': 175.0, 'JPM': 210.0, 'BAC': 42.0
    }
    base = base_prices[symbol]
    change = random.uniform(-2.0, 2.0)
    price = round(base + change, 2)
    
    return {
        "symbol": symbol,
        "price": price,
        "volume": random.randint(100000, 2000000),
        "timestamp": datetime.now().isoformat(),
        "change_pct":

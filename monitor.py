import time
import requests

URL = "http://127.0.0.1:8000/generate"

def monitor_system():
    prompt = "Hello, how are you?"
    response = requests.post(URL, params={"prompt": prompt}).json()

    latency = response["latency_seconds"]
    print(f"Latency: {latency:.4f}s")

    # Simple alert rule (like Prometheus alert)
    if latency > 1.0:
        print("⚠️ ALERT: High latency detected!")

while True:
    monitor_system()
    time.sleep(2)


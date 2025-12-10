import requests
import time
import concurrent.futures

URL = "http://127.0.0.1:8000/generate"

def send_request(prompt="Hello!"):
    start = time.time()
    response = requests.post(URL, params={"prompt": prompt}).json()
    return time.time() - start

def run_load_test(concurrency):
    print(f"\nRunning load test with {concurrency} parallel requests…")

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request) for _ in range(concurrency)]
        latencies = [f.result() for f in futures]

    avg_latency = sum(latencies) / len(latencies)
    print(f"Average latency: {avg_latency:.4f}s")

    # Simulate autoscaling logic
    if avg_latency > 1.0:
        print("⚠️ DECISION: Scale Up — Latency too high")
    else:
        print("✓ System healthy")

# Test with different load levels
run_load_test(1)
run_load_test(5)
run_load_test(15)
run_load_test(30)


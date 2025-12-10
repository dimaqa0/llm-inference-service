from fastapi import FastAPI, Query
from model import generate_text
import logging

app = FastAPI()

# Logging setup
logging.basicConfig(
    filename="service.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.post("/generate")
def generate(prompt: str = Query(..., description="Text prompt for generation")):
    text, latency = generate_text(prompt)

    # Log every request
    logging.info(f"Prompt length={len(prompt)}, Latency={latency:.4f}s")

    return {
        "generated_text": text,
        "latency_seconds": latency
    }

@app.get("/health")
def health():
    return {"status": "ok"}


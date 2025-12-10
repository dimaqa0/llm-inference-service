# Mini LLM Inference Service with Monitoring & Load Simulation

A production-ready LLM inference service demonstrating SRE principles: observability, monitoring, load testing, and autoscaling logic.

## 📁 Project Structure

```
project/
│── app.py          # FastAPI service with logging
│── model.py        # LLM inference logic
│── monitor.py      # Monitoring & alerting system
│── load_test.py    # Load testing & autoscaling simulation
│── requirements.txt # Python dependencies
│── INTERVIEW_GUIDE.md # Detailed explanations for interview
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Service

```bash
uvicorn app:app --reload
```

The service will be available at `http://127.0.0.1:8000`

### 3. Test the API

- Interactive docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`
- Generate endpoint: `POST http://127.0.0.1:8000/generate?prompt=Hello`

### 4. Run Monitoring (in separate terminal)

```bash
python monitor.py
```

### 5. Run Load Test

```bash
python load_test.py
```

## 📚 What This Project Demonstrates

- ✅ **LLM Inference**: Tokenization, model loading, text generation
- ✅ **REST API**: FastAPI service with health checks
- ✅ **Observability**: Request logging with metrics
- ✅ **Monitoring**: Continuous health checks with alerting
- ✅ **Load Testing**: Concurrent request simulation
- ✅ **Autoscaling Logic**: Scale-up decisions based on latency

## 📖 Detailed Explanations

See `INTERVIEW_GUIDE.md` for comprehensive explanations of every component, perfect for interview preparation.

## 🛠️ Technologies Used

- **FastAPI**: Modern Python web framework
- **Transformers**: Hugging Face library for LLMs
- **Uvicorn**: ASGI web server
- **Python**: Core language

## 💼 Interview Talking Points

This project showcases the same SRE principles used in production AI systems:

- Service reliability and health monitoring
- Performance measurement and optimization
- Capacity planning through load testing
- Automated scaling based on metrics

---

**Built for Qualcomm SRE Interview Preparation**

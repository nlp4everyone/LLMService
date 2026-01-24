# 🚀 Introduction:

This project provides a production-ready setup for serving Large Language Models (LLMs) using vLLM
, with integrated observability powered by Prometheus, Grafana, and NVIDIA DCGM Exporter for GPU monitoring.
<br/>

# 🧩 Components Overview
### 🔹 vLLM

- High-throughput and memory-efficient inference engine for large language models.

- Supports continuous batching, tensor parallelism, and streaming outputs.

- Exposes OpenAI-compatible REST API for easy integration.

### 🔹 Prometheus

- Time-series database and monitoring system.

- Scrapes metrics from vLLM and DCGM exporters.

- Provides query capabilities (PromQL) for monitoring model performance.

### 🔹 Grafana

- Visualization layer on top of Prometheus.

- Pre-built dashboards for:

- vLLM request/latency statistics

- GPU utilization, memory usage, power consumption

- Overall system health

### 🔹 NVIDIA DCGM Exporter

- NVIDIA’s Data Center GPU Manager metrics exporter.

- Exposes GPU-level metrics like utilization %, memory usage, temperature, power draw.

- Integrated with Prometheus for long-term monitoring.
<br/>

# ⚙️ Installation
1. Clone the repository:
```
git clone -b engine/vllm https://github.com/nlp4everyone/PrivateAI.git
```
```
cd PrivateAI
```

2. Start Services with Docker Compose:
```
bash run_service.sh
```

3. Access Dashboards

vLLM API → http://localhost:8100

Prometheus UI → http://localhost:9090

Grafana UI → http://localhost:3000
 (default user: admin, pass: admin)
<br/>

# 📊 Metrics
1. vLLM Metrics
Exposed at /metrics endpoint (Prometheus format). Key metrics:

- vllm:e2e_request_latency_seconds_bucket → End to end request latency measured in seconds

- vllm:time_per_output_token_seconds → Inter token latency (Time Per Output Token, TPOT) in second.

- vllm:time_to_first_token_seconds → Time to First Token (TTFT) latency in seconds.

- vllm:request_queue_time_seconds →  Queue Time

Reference: https://docs.vllm.ai/en/v0.8.5/design/v1/metrics.html
<br/>

2. GPU Metrics (DCGM)
- DCGM_FI_DEV_FB_USED → GPU framebuffer (memory) used (MiB)
  
- DCGM_FI_DEV_POWER_USAGE → Power consumption (Watts)

- DCGM_FI_DEV_GPU_TEMP → GPU temperature (°C)

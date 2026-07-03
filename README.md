# 🚀 Private LLM with SGLang

This project sets up a local language model serving environment using SGLang, optimized for GPU acceleration with Nvidia GPUs.

## 🛠 Prerequisites

### 💻 Hardware Requirements
- Nvidia GPU with Compute Capability 7.0 or higher (Turing, Ampere, or newer architecture recommended)
- At least 8GB of GPU VRAM
- 16GB+ system RAM

### 📋 Software Requirements
- Linux-based operating system (Ubuntu 20.04/22.04 recommended)
- Nvidia Driver 535.54.03 or later
- CUDA 12.8 or higher
- Docker 20.10.0 or later
- Docker Compose v2.0.0 or later
- Nvidia Container Toolkit

## ⚙️ Configuration

### 🔧 Environment Variables
Create a `.env` file in the project root with your preferred configuration:

```bash
# Model configuration
MODEL_NAME=Qwen/Qwen3-4B-AWQ  # Default model

# Port configuration
SGLANG_PORT=30000

# GPU configuration (comma-separated list of GPU indices)
CUDA_VISIBLE_DEVICES=0
```

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   # Clone the main repository
   git clone -b engine/sglang https://github.com/nlp4everyone/LLMService.git
   # Navigate to project directory
   cd LLMService
   ```

2. **Build and start the services**
   ```bash
   # Start all services in detached mode
   make up
   ```

3. **Verify the service is running**
   ```bash
   curl http://localhost:30000/health
   ```

## 🔍 Troubleshooting

### ⚠️ Nvidia Driver Issues
- If you get `NVIDIA-SMI has failed` error, verify your Nvidia drivers are installed correctly:
  ```bash
  nvidia-smi
  ```
- If the command is not found, reinstall Nvidia drivers and reboot your system.

### 🔄 CUDA Version Mismatch
- If you encounter CUDA version errors, ensure you have CUDA 12.8 or higher installed:
  ```bash
  nvcc --version
  ```


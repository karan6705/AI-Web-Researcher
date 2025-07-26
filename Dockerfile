FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    procps \
    libxss1 \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN wget https://github.com/ollama/ollama/releases/latest/download/ollama-linux-amd64.tgz -O /tmp/ollama.tgz \
    && tar -xzf /tmp/ollama.tgz -C /usr/local/bin/ \
    && chmod +x /usr/local/bin/ollama \
    && rm /tmp/ollama.tgz

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium
RUN playwright install-deps

# Copy application files
COPY . .

# Expose port
EXPOSE 8501

# Create startup script
RUN echo '#!/bin/bash\n\
# Start Ollama in background\n\
ollama serve &\n\
sleep 5\n\
# Pull default model\n\
ollama pull llama3.1:8b &\n\
# Start Streamlit\n\
streamlit run main.py --server.port 8501 --server.address 0.0.0.0\n\
' > /app/start.sh && chmod +x /app/start.sh

# Set the default command
CMD ["/app/start.sh"] 

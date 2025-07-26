# AI Web Scraper

A powerful web scraping application with AI-powered content parsing using multiple language models.

## Features

- 🌐 **Web Scraping**: Extract content from any website using Playwright
- 🤖 **AI-Powered Parsing**: Multiple AI models for content analysis
- 🎯 **Model Selection**: Choose from llama3.1, mistral, codellama, and more
- 📊 **Clean Interface**: Streamlit-based web interface
- 🔄 **Batch Processing**: Handle large content in chunks

## Available AI Models

- **llama3.1**: Most advanced - Best for complex content parsing
- **llama3.1:8b**: Faster version with good accuracy
- **mistral:7b**: Excellent for text understanding and extraction
- **codellama:7b**: Great for structured data and technical content
- **phi3**: Lightweight - Fast but less accurate

## Local Development

### Prerequisites

- Python 3.8+
- Ollama installed and running
- At least 8GB RAM (for AI models)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AI-Webscraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

4. **Start Ollama and pull models**
   ```bash
   ollama serve
   ollama pull llama3.1:8b
   ollama pull mistral:7b
   ollama pull codellama:7b
   ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

## Deployment Options

### 1. Streamlit Cloud (Recommended for Demo)

**Pros**: Easy deployment, free tier, built for Streamlit
**Cons**: Limited resources, need to handle Ollama differently

**Steps**:
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Deploy (note: will need to modify for cloud Ollama)

### 2. Railway

**Pros**: Easy deployment, good free tier, supports Docker
**Cons**: Need to handle Ollama models

**Steps**:
1. Push code to GitHub
2. Connect Railway to GitHub
3. Deploy using Dockerfile

### 3. Google Cloud Run

**Pros**: Scalable, pay-per-use, good for production
**Cons**: More complex setup

**Steps**:
1. Build and push Docker image
2. Deploy to Cloud Run
3. Configure memory limits (8GB+ recommended)

### 4. Local Docker

**For testing deployment locally**:

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t ai-webscraper .
docker run -p 8501:8501 --memory=8g ai-webscraper
```

## Environment Variables

- `OLLAMA_HOST`: Ollama server host (default: localhost)
- `OLLAMA_PORT`: Ollama server port (default: 11434)

## Usage

1. **Select AI Model**: Choose the model that best fits your needs
2. **Enter URL**: Paste any website URL
3. **Scrape**: Click "Scrape Website" to extract content
4. **Parse**: Describe what you want to extract and get AI-powered results

## Model Recommendations

- **General content**: llama3.1
- **Speed**: llama3.1:8b or mistral:7b
- **Technical data**: codellama:7b
- **Lightweight**: phi3

## Troubleshooting

### Memory Issues
- Ensure at least 8GB RAM available
- Use smaller models (8b variants)
- Increase swap space

### Ollama Connection
- Ensure Ollama is running: `ollama serve`
- Check models are downloaded: `ollama list`

### Browser Issues
- Ensure Playwright browsers are installed
- Run: `playwright install chromium`

## License

MIT License

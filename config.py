# AI Model Configuration
# Available models for web scraping and content parsing

AVAILABLE_MODELS = {
    "llama3.1": "llama3.1",  # Most advanced, best for complex parsing
    "llama3.1-8b": "llama3.1:8b",  # Faster version of llama3.1
    "mistral": "mistral:7b",  # Excellent for text understanding and extraction
    "codellama": "codellama:7b",  # Good for structured data extraction
    "phi3": "phi3",  # Lightweight but less accurate
}

# Default model to use
DEFAULT_MODEL = "llama3.1"

# Model descriptions for UI
MODEL_DESCRIPTIONS = {
    "llama3.1": "Most advanced - Best for complex content parsing and analysis",
    "llama3.1-8b": "Faster version - Good balance of speed and accuracy",
    "mistral": "Excellent for text understanding and information extraction",
    "codellama": "Great for structured data and technical content",
    "phi3": "Lightweight - Fast but less accurate for complex tasks"
}

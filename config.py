 # AI Model Configuration
# Available models for web scraping and content parsing using Google Gemini API

AVAILABLE_MODELS = {
    "gemini-1.5-flash": "gemini-1.5-flash",  # Fastest, good for most tasks
    "gemini-1.5-pro": "gemini-1.5-pro",  # Most advanced, best for complex parsing
    "gemini-1.0-pro": "gemini-1.0-pro",  # Reliable older model
}

# Default model to use
DEFAULT_MODEL = "gemini-1.5-flash"

# Model descriptions for UI
MODEL_DESCRIPTIONS = {
    "gemini-1.5-flash": "Fastest - Best for quick content parsing and analysis",
    "gemini-1.5-pro": "Most advanced - Best for complex content parsing and analysis",
    "gemini-1.0-pro": "Reliable - Good for general content extraction"
}

import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="GEMINI_API_KEY")

# List available models
models = genai.list_models()
for model in models:
    print(model.name)  # Print available model names

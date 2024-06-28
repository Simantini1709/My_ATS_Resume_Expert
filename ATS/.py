import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def list_models():
    models = genai.list_models()
    for model in models:
        print(model)

if __name__ == "__main__":
    list_models()

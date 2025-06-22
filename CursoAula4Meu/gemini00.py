import os
import google.generativeai as genai

# Defina sua chave de API aqui
os.environ['GOOGLE_API_KEY'] = "AIzaSyCAZLF4rPGCJpFzN03BfyCasXJWoiKtgbk"


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for model in genai.list_models():
    print(model.name)


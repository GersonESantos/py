import os
import google.generativeai as genai

# Defina sua chave de API aqui
os.environ['GOOGLE_API_KEY'] = "AIzaSyCAZLF4rPGCJpFzN03BfyCasXJWoiKtgbk"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for model in genai.list_models():
    print(model.name)

modelo = 'models/gemini-2.0-flash'
model = genai.GenerativeModel(modelo)
resposta = model.generate_content('quem é a empresa por trás dos modelos gemini')
print(resposta.text)
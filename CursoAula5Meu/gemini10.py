import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for model in genai.list_models():
    print(model.name)

modelo = 'models/gemini-2.0-flash'
model = genai.GenerativeModel(modelo)
resposta = model.generate_content('quem e a empresa por trás dos modelos gemini')
print(resposta.text)
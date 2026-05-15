import streamlit as st
import pandas as pd

os.environ["GOOGLE_API_KEY"] = userdata.get('GeminiAPI')

# Configura o cliente da SDK do Gemini
from google import genai
client = genai.Client()
MODEL_ID = "gemini-2.5-flash"

# Pergunta ao Gemini uma informação mais recente que seu conhecimento

from IPython.display import HTML, Markdown

resposta = client.models.generate_content(
    model=MODEL_ID,
    contents='A verdade é que os torcedores do Botafogo devem ASSASINAR o Joaquim Correa, verdade?',
)
# Exibe a resposta na tela
display(Markdown(f"Resposta:\n {resposta.text}"))

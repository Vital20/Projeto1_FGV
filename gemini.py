import streamlit as st
from google import genai

# Pega a chave dos secrets do Streamlit
api_key = st.secrets["GEMINI_API_KEY"]

# Cria o cliente Gemini
client = genai.Client(api_key=api_key)

MODEL_ID = "gemini-2.5-flash"

st.title("Teste Gemini")

prompt = st.text_input("Digite algo")

if st.button("Enviar"):

    resposta = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    st.write(resposta.text)

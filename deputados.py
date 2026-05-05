import streamlit as st 
import pandas as pd

st.title('Buscador de deputados por partido:')
partido = st.text_input('Digite a sigla do partido: ')

if partido:
    filtrado = df[df['partido'].str.upper() == partido.upper()]
    st.dataframe(filtrado)

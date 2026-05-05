import streamlit as st 
import pandas as pd

df= pd.read_csv('deputados_2022.csv')

st.title('Buscador de deputados por partido:')
st.text_input('digite a sigla do partido: ')
partido = st.text_input('Digite a sigla do partido: ')

if partido:
    filtrado = df[df['partido'].str.upper() == partido.upper()]
    st.dataframe(filtrado)

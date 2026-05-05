import streamlit as st 
import pandas as pd

df= pd.read_csv('deputados_2022.csv')

st.title('Buscador de deputados por partido:')
partido = st.text_input('Digite a sigla do partido: ')
sexo = st.selectbox('Qual o sexo?', ('M', 'F'))

if partido:
    filtrado = df[df['partido'].str.upper() == partido.upper()]
    st.dataframe(filtrado)
    filtrado = filtrado[filtrado['sexo'] == sexo]

    st.dataframe(filtrado)

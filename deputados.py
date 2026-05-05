import streamlit as st 
import pandas as pd

df= pd.read_csv('deputados_2022.csv')
st.dataframe(df)

st.title('Buscador de deputados por partido:')
st.text_input('digite a sigla do partido: ')

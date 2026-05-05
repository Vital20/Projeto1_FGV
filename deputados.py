import streamlit as st 
import pandas as pd

df= pd.read_csv('deputados_2022.csv')

st.title('Buscador de deputados por partido:')
partido = st.text_input('Digite a sigla do partido: ')
sexo = st.selectbox('Qual o sexo?', ('M', 'F'))

if partido:
    filtrado = df[df['partido'].str.upper() == partido.upper()]
    filtrado = filtrado[filtrado['sexo'] == sexo]

    st.dataframe(filtrado)

    contagem = filtrado['sexo'].value_counts()

    fig, ax = plt.subplots()
    ax.bar(contagem.index, contagem.values)
    ax.set_title('Quantidade por sexo')
    ax.set_xlabel('Sexo')
    ax.set_ylabel('Quantidade')

    st.pyplot(fig)

import streamlit as st

st.title('Botafogo em Copas do Mundo da Seleção brasileira')
st.subheader('Por: Arthur Vital')
st.write("""
O Botafogo é um dos clubes mais tradicionais do Brasil, sendo peça fundamental
em momentos históricos da Seleção Brasileira, especialmente nas Copas do Mundo.
Mas como essa relação começou? E por que o clube é tão importante nesse contexto?
""")

st.image('https://s2-oglobo.glbimg.com/5mQLlKwt25ljz6ZCj0RXzCuOBzI=/0x0:2000x1194/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_da025474c0c44edd99332dddb09cabe8/internal_photos/bs/2024/q/e/zhOyUtR5Kw92vopn1zAw/arte-40-.png' , caption='Jairzinho, Luiz Henrique e Igor Jesus')
st.divider()

st.header("Momentos históricos: ")

copa = st.selectbox(
    "Escolha uma Copa do Mundo",
    ["1958", "1962", "1970"]
)

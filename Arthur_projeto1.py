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

if copa == "1958":
    st.image("https://crfb.museudofutebol.org/anexos/imagem/499456/w:640/h:640/c:0", caption="Seleção de 1958")
    st.write("""
    A Copa de 1958 marca o início de uma hegemonia do futebol brasileiro no mundo, e o Botafogo teve papel crucial nisso.
    
    Jogadores como Garrincha e Nilton Santos foram fundamentais na campanha, trazendo um estilo de jogo ofensivo,
    técnico e criativo que encantou o mundo.
    
    Garrincha, principalmente, foi decisivo nos momentos mais importantes, sendo considerado um dos grandes nomes
    daquela conquista. Já Nilton Santos criou a posição "lateral", apoiando o ataque de forma inédita.
    """)

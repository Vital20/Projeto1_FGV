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
    
    Impossível não destacar Garrincha e Nilton Santos, eles foram fundamentais na campanha, trazendo um estilo de jogo ofensivo,
    técnico e criativo que encantou o mundo.
    
    Garrincha, principalmente, foi decisivo nos momentos mais importantes, sendo considerado um dos grandes nomes
    daquela conquista. Já Nilton Santos criou a posição "lateral", apoiando o ataque de forma inédita.
    """)
    # 👇 AQUI entram as imagens depois do texto
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://p2.trrsf.com/image/fget/cf/1200/1600/middle/images.terra.com/2022/12/01/1261386654-garrincha-drible.jpg", caption="Garrincha", use_container_width=True)

    with col2:
        st.image("https://terceirotempo.uol.com.br/imagens/31/71/w500_h140_qfl_fto_13171.webp", caption="Nilton Santos", use_container_width=True)

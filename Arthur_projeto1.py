import streamlit as st
import pandas as pd

st.sidebar.title("Navegação")
st.sidebar.write("Explore as Copas e o impacto do Botafogo!")

pagina = st.sidebar.selectbox(
    "Explorar",
    ["História (Copas)", "Rumo a 2026"]
)

if pagina == "História em Copas":

    st.title('Botafogo em Copas do Mundo da Seleção brasileira')
    st.subheader('Por: Arthur Vital')

    st.write("""
    O Botafogo é um dos clubes mais tradicionais do Brasil, sendo peça fundamentalem momentos históricos da Seleção Brasileira, especialmente nas Copas do Mundo.
    Mas como essa relação começou? E por que o clube é tão importante nesse contexto?
    """)

    st.image('https://s2-oglobo.glbimg.com/5mQLlKwt25ljz6ZCj0RXzCuOBzI=/0x0:2000x1194/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_da025474c0c44edd99332dddb09cabe8/internal_photos/bs/2024/q/e/zhOyUtR5Kw92vopn1zAw/arte-40-.png' , caption='Jairzinho, Luiz Henrique e Igor Jesus')

    st.write("Veja o gráfico da quantidade de jogadores no time titular de cada ano da seleção que pertencia ao Botafogo de Futebol e Regatas:")

    dados = pd.DataFrame({
        "Copa": ["1958", "1962", "1970"],
        "Jogadores do Botafogo": [3, 5, 1]})

    st.bar_chart(dados.set_index("Copa"))

    st.divider()

    st.header("Momentos históricos: ")

    copa = st.selectbox(
        "Escolha uma Copa do Mundo",
        ["1958", "1962", "1970"]
    )

    if copa == "1958":
        st.title("O começo de tudo:")
        
        st.image("https://crfb.museudofutebol.org/anexos/imagem/499456/w:640/h:640/c:0", caption="Seleção de 1958")
        st.write("""
        A Copa de 1958 marca o início de uma hegemonia do futebol brasileiro no mundo, e o Botafogo teve papel crucial nisso.
        
        Impossível não destacar Garrincha e Nilton Santos, eles foram fundamentais na campanha, trazendo um estilo de jogo ofensivo,
        técnico e criativo que encantou o mundo. Além deles, Didi, que foi eleito o melhor jogador da Copa de 1958 também era o jogador do glorioso.
        
        Falando de Garrincha, ele foi decisivo nos momentos mais importantes - destruiu a seleção da URSS. Foi considerado um dos grandes nomes
        daquela conquista. Já Nilton Santos criou a posição "lateral", apoiando o ataque de uma forma nunca vista antes.
        """)
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://auniao.pb.gov.br/noticias/caderno_esporte/morte-de-mane-garrincha-que-jogou-tambem-por-times-paraibanos-completa-34-anos/mane.jpg/@@images/7b153cd0-2c8c-4f4e-9e0b-ed17a5f7abc9.jpeg", caption="Garrincha", use_container_width=True)

        with col2:
            st.image("https://terceirotempo.uol.com.br/imagens/31/71/w500_h140_qfl_fto_13171.webp", caption="Nilton Santos", use_container_width=True)

        with col3:
            st.image("https://p2.trrsf.com/image/fget/cf/1200/900/middle/images.terra.com/2022/11/30/1732884753-didi-selecao-brasileira.jpeg", caption="Didi", use_container_width=True)

    elif copa == "1962":
        st.title("A SELEFOGO:")
                
        st.image("https://lncimg.lance.com.br/cdn-cgi/image/width=950,quality=75,fit=pad,format=webp/uploads/2019/03/12/5c879f3beafe5.jpeg", caption="Seleção de 1962")

        st.write("""
        Pelé se lesiona... e agora? Quem irá levar o Brasil ao troféu?
        

        PERDEU, MANÉ! Garrincha foi o nome da Copa. O Ponta do Botafogo, assumiu o protagonismo e protagonizou uma das maiores atuações individuais da história das Copas.


        A Seleção de 1962 tinha uma base MUITO forte do Botafogo. Em vários momentos,
        o time titular contava com diversos jogadores do clube - Garrincha, Nilton Santos, Didi, Amarildo e Zagallo. Isso mostra o nível absurdo
        daquele elenco alvinegro na época.


        Era um time extremamente coletivo que contavam com diversos craques
        """)

        st.image("https://pbs.twimg.com/media/FiAkFK3WIAMzJ7i.jpg", caption="Os jogadores do Botafogo na Seleção")

    elif copa == "1970":
        st.title("O auge do futebol arte:")

        st.image("https://crfb.museudofutebol.org/anexos/imagem/511247/w:640/h:640/c:0", caption="Seleção Brasileira de 1970")

        st.write("""
        Se 1962 foi a 'Selefogo', 1970 foi o auge do futebol arte.

        A Seleção Brasileira chegou no México com um dos times mais talentosos de toda a história,
        e no meio de tantos craques, tinha um jogador do Botafogo que fez história:

        Jairzinho.

        O ponta herdou a camisa 7, de botafoguense para botafoguense, e fez algo que até hoje ninguém mais conseguiu:
        marcou gol em TODOS os jogos da Copa do Mundo.

        Mesmo em uma seleção recheada de lendas como Pelé, Tostão e Rivelino,
        o jogador do Botafogo teve protagonismo real.

        A consagração do futebol brasileiro para o mundo.
        """)

        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS49c4Wwq9NXmeD5NWVMUoCepaoxojOY1IUwQ&s",caption="Jairzinho - o Furacão da Copa",use_container_width=True)

        st.success("Jairzinho marcou em todos os jogos da Copa de 1970 — um feito histórico.")

    st.divider()
    st.header("Sem voltar pra ler, quiz do torcedor")

    pontuacao = 0

    q1 = st.radio(
        "Quem marcou em todos os jogos da Copa de 1970?",
        ["Pelé", "Jairzinho", "Tostão"])

    if q1 == "Jairzinho":
        pontuacao += 1

    q2 = st.radio(
        "Quantos jogadores do Botafogo estavam na Copa de 1958?",
        ["2", "3", "5"]
    )

    if q2 == "2":
        pontuacao += 1

    if st.button("Ver resultado"):
        st.write(f"Pontuação: {pontuacao}/2")

        if pontuacao == 2:
            st.success("Sabe muito")
        else:
            st.warning("👀")

# 2026

elif pagina == "Rumo a 2026":
    st.title("Botafogo rumo à Copa de 2026:")

    st.write("""
    Se no passado o Botafogo foi protagonista, agora a pergunta é:
    quem pode representar o clube em 2026?
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Danilo")
        st.image("https://i.metroimg.com/OeCs287XzArnqE9vtRDd92NLAXBhD-TatkL6GxIvm50/w:900/q:85/f:webp/plain/https://images.metroimg.com/2026/01/55068194828_bc5100abaa_k.jpg")
        st.write("Certamente vai próxima Copa, prinicipal jogador do atual elenco de 26.")

    with col2:
        st.subheader("Luiz Henrique")
        st.image("https://jpimg.com.br/uploads/2024/11/luiz-henrique-676x450.jpg")
        st.write("Ex-jogador do Botafogo e um dos principais jogadores da campanha histórica de 2024")

    with col3:
        st.subheader("Igor Jesus")
        st.image("https://meubotafogo.com.br/wp-content/uploads/2024/10/54089673649_2538fdf4b8_c.jpg")
        st.write("Ex-Botafogo e um dos protagonistas de 2024 que vem sendo um dos observados para a Copa")













              

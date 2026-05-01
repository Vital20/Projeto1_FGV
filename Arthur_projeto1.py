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
    st.title("O começo de tudo:")
    
    st.image("https://crfb.museudofutebol.org/anexos/imagem/499456/w:640/h:640/c:0", caption="Seleção de 1958")
    st.write("""
    A Copa de 1958 marca o início de uma hegemonia do futebol brasileiro no mundo, e o Botafogo teve papel crucial nisso.
    
    Impossível não destacar Garrincha e Nilton Santos, eles foram fundamentais na campanha, trazendo um estilo de jogo ofensivo,
    técnico e criativo que encantou o mundo.
    
    Garrincha, principalmente, foi decisivo nos momentos mais importantes - destruiu a seleção da URSS. Foi considerado um dos grandes nomes
    daquela conquista. Já Nilton Santos criou a posição "lateral", apoiando o ataque de uma forma nunca vista antes.
    """)
    
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://auniao.pb.gov.br/noticias/caderno_esporte/morte-de-mane-garrincha-que-jogou-tambem-por-times-paraibanos-completa-34-anos/mane.jpg/@@images/7b153cd0-2c8c-4f4e-9e0b-ed17a5f7abc9.jpeg", caption="Garrincha", use_container_width=True)

    with col2:
        st.image("https://terceirotempo.uol.com.br/imagens/31/71/w500_h140_qfl_fto_13171.webp", caption="Nilton Santos", use_container_width=True)
        
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

    st.image("https://upload.wikimedia.org/wikipedia/commons/7/74/Brazil_1970.JPG", caption="Seleção Brasileira de 1970")

    st.write("""
    Se 1962 foi a 'Selefogo', 1970 foi o auge do futebol arte.

    A Seleção Brasileira chegou no México com um dos times mais talentosos de toda a história,
    e no meio de tantos craques, tinha um jogador do Botafogo que fez história:

    Jairzinho.

    O ponta herdou a camisa 7, de botafoguense para botafoguense, e fez algo que até hojeninguém mais conseguiu:
    marcou gol em TODOS os jogos da Copa do Mundo.

    Mesmo em uma seleção recheada de lendas como Pelé, Tostão e Rivelino,
    o jogador do Botafogo teve protagonismo real.

    A consagração do futebol brasileiro para o mundo.
    """)

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3e/Jairzinho_1970.jpg",
        caption="Jairzinho - o Furacão da Copa",
        use_container_width=True
    )

    st.success("⚫⚪ Jairzinho marcou em todos os jogos da Copa de 1970 — um feito histórico.")












              

# 08 — Clusterização (agrupar sem rótulo)

**Como identificar:** **não existe variável-alvo**. A pergunta é "que grupos
existem nessas publicações?", "como segmentar o público/perfis?", e não
"prever X". É o **aprendizado não supervisionado** (Aula 13).

⚠️ Mesmo quando a questão é de regressão ou classificação, o enunciado
costuma pedir que você **explique por que não é clusterização** — a resposta
pronta está no fim deste arquivo.

## Passo a passo

### 1. Escolher e preparar as variáveis

```python
COLS = ["seguidores_autor", "tamanho_legenda", "n_hashtags",
        "taxa_engajamento_pct"]           # 🔧 numéricas que descrevem o perfil

base = df[COLS].dropna().copy()
```

Aqui **pode** usar variáveis de resultado (`taxa_engajamento_pct`, `alcance`):
não há previsão, então não existe vazamento. O critério é outro — as
variáveis devem fazer sentido juntas para descrever o que você quer agrupar.

Se precisar incluir categoria: `pd.get_dummies(..., dtype=int)` antes.

### 2. Escalonar — obrigatório

```python
from sklearn.preprocessing import StandardScaler

escalador = StandardScaler()
X = escalador.fit_transform(base)
```

Sem escalonar, `seguidores_autor` (dezenas de milhares) domina
`n_hashtags` (0 a 15) e o KMeans agrupa praticamente só por seguidores.
**Escalonar é o passo que mais cai em prova de clusterização.**

### 3. Escolher o k

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X)
    print(f"k={k} | inércia={km.inertia_:.1f} | silhueta={silhouette_score(X, km.labels_):.3f}")
```

Dois critérios:
- **Cotovelo (inércia):** a inércia sempre cai quando k aumenta; procure o
  ponto em que ela **para de cair rápido**.
- **Silhueta:** vai de -1 a 1; **quanto maior, melhor** a separação. Valores
  perto de 0 indicam grupos mal definidos (e é um resultado legítimo de
  reportar).

Gráfico do cotovelo:
```python
ks, inercias = range(2, 8), []
for k in ks:
    inercias.append(KMeans(n_clusters=k, random_state=42, n_init=10).fit(X).inertia_)

plt.figure(figsize=(7, 4))
plt.plot(list(ks), inercias, marker="o")
plt.title("Método do cotovelo — escolha de k")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Inércia")
plt.tight_layout(); plt.show()
```

### 4. Ajustar e rotular

```python
km = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)   # 🔧 k escolhido
base["cluster"] = km.labels_
```

### 5. Interpretar os grupos (a parte que vale nota)

```python
perfil = base.groupby("cluster")[COLS].mean().round(2)
print(perfil)
print(base["cluster"].value_counts().sort_index())
```

Agora **dê nome aos grupos** com base nos números. Exemplo de leitura:

> O cluster 2 reúne publicações com legendas longas e muitas hashtags, mas
> taxa de engajamento acima da média; o cluster 0 concentra peças de legenda
> curta e poucas hashtags, com engajamento típico mais baixo.

Isso é o que o enunciado chama de "interpretação dos clusters". Sem nomear e
descrever, a questão fica incompleta.

Visualizar (duas variáveis por vez):
```python
plt.figure(figsize=(7, 5))
plt.scatter(base["seguidores_autor"], base["taxa_engajamento_pct"],
            c=base["cluster"], cmap="viridis", alpha=0.7)
plt.title("Grupos de publicações identificados pelo KMeans")
plt.xlabel("Seguidores do autor"); plt.ylabel("Taxa de engajamento (%)")
plt.colorbar(label="Cluster")
plt.tight_layout(); plt.show()
```

---

## Os três tipos de aprendizado (decore esta tabela)

| | Tem alvo? | Alvo é... | Exemplo no festival |
|---|---|---|---|
| **Regressão** | sim | número contínuo | estimar a taxa de engajamento esperada |
| **Classificação** | sim | categoria | prever se merece divulgação adicional |
| **Clusterização** | **não** | — | descobrir perfis de publicação sem rótulo prévio |

## Resposta escrita — "por que NÃO é clusterização"

> Clusterização não responde a essa pergunta porque é um método **não
> supervisionado**: ela agrupa registros semelhantes sem usar um rótulo
> conhecido. Aqui já sabemos o valor correto de cada publicação na base, e o
> objetivo é **prever** esse valor para peças novas — o que exige um método
> supervisionado.

## Resposta escrita — "por que É clusterização"

> É um caso de clusterização porque não há variável-alvo definida: nenhuma
> coluna indica previamente a que grupo cada publicação pertence. O objetivo é
> **descobrir** agrupamentos a partir da semelhança entre as características,
> e não prever um valor conhecido. Como os grupos são construídos pelo
> algoritmo, eles não têm significado objetivo por si só — a interpretação e a
> escolha de k envolvem julgamento, e um k diferente produziria outra
> segmentação igualmente válida.

## Armadilhas

- **Esquecer de escalonar** é o erro nº 1.
- `n_init=10` evita aviso e resultado instável em versões novas do sklearn.
- `random_state=42` sempre — senão os rótulos dos clusters mudam a cada
  execução.
- Os **números dos clusters não têm ordem**: cluster 2 não é "melhor" que o 0,
  é só um rótulo. Nunca trate como escala.
- Silhueta baixa (≈0,2) significa grupos pouco separados — reporte
  honestamente, não force uma narrativa.

# 06 — Regressão (prever um número)

**Como identificar:** o alvo é **numérico contínuo** (taxa esperada, alcance
esperado, tempo, preço). Se o alvo fosse categoria → `07-classificacao.md`.
Se não houvesse alvo → `08-clusterizacao.md`.

## Passo a passo completo

### 1. Escolher as características (sem vazamento)

```python
FEATURES = [
    "tema", "formato", "seguidores_autor", "videos_autor",
    "tamanho_legenda", "n_emojis", "n_hashtags", "hora",
    "dia_semana", "duracao_segundos",
]                                          # 🔧 exatamente as permitidas
ALVO = "taxa_engajamento_pct"              # 🔧
```

🚨 **Vazamento de dados (data leakage).** Se a pergunta é "estimar *antes* de
publicar", não pode entrar nada que só existe **depois** da publicação:
`alcance`, `interacoes`, `compartilhamentos`, `salvamentos`, nem nada
derivado do alvo (`taxa_utilidade_pct`, por exemplo). Também fora:
`id_publicacao` (identificador não é informação). O enunciado costuma listar
as permitidas — use a lista dele, sem acrescentar.

### 2. Categoria vira número

```python
X = pd.get_dummies(df[FEATURES], columns=["tema", "formato"],
                   drop_first=True, dtype=int)
y = df[ALVO]
```

- `drop_first=True` evita colunas redundantes (com 4 temas, 3 colunas bastam).
- `dtype=int` produz 0/1 em vez de `True/False` — evita dor de cabeça.

### 3. Separar treino e teste

```python
from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

`test_size=0.25` = "reserve 25% para teste". Em **regressão não se usa
`stratify`** (isso é coisa de classificação).

### 4. Ajustar os modelos

```python
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

linear = LinearRegression().fit(X_treino, y_treino)
arvore = DecisionTreeRegressor(max_depth=4, random_state=42).fit(X_treino, y_treino)
```

Outros que podem ser pedidos:
```python
from sklearn.ensemble import RandomForestRegressor
floresta = RandomForestRegressor(random_state=42).fit(X_treino, y_treino)
```

### 5. Comparar com MAE e R²

```python
from sklearn.metrics import mean_absolute_error, r2_score

linhas = []
for nome, modelo in [("Regressão linear", linear), ("Árvore de regressão", arvore)]:
    previsto = modelo.predict(X_teste)
    linhas.append({
        "modelo": nome,
        "MAE": mean_absolute_error(y_teste, previsto),
        "R2": r2_score(y_teste, previsto),
    })

tabela = pd.DataFrame(linhas).sort_values("MAE")   # menor MAE primeiro
print(tabela)
```

### 6. Gráfico real × previsto (do modelo escolhido)

```python
melhor = linear if tabela.iloc[0]["modelo"] == "Regressão linear" else arvore
y_previsto = melhor.predict(X_teste)
```
Template do gráfico em `04-graficos.md` → "Dispersão — real × previsto".

---

## O que cada métrica significa (isso cai na resposta escrita)

**MAE — erro absoluto médio.** Em média, o quanto a previsão erra, **na mesma
unidade do alvo**. MAE de 3,8 numa taxa em % significa "em média a previsão
erra 3,8 pontos percentuais". Quanto menor, melhor. Fácil de explicar para
não-técnicos — por isso o enunciado usa ele como critério.

**R² — coeficiente de determinação.** Quanto da variação do alvo o modelo
consegue explicar. 1 = perfeito; 0 = igual a chutar sempre a média;
**negativo = pior do que chutar a média** (acontece de verdade, e é um
resultado válido para reportar, não um erro seu).

**RMSE** (se pedirem): parecido com o MAE, mas penaliza mais erros grandes.
```python
from sklearn.metrics import mean_squared_error
rmse = mean_squared_error(y_teste, previsto) ** 0.5
```

## Coeficientes da regressão linear (se pedirem interpretação)

```python
coef = pd.Series(linear.coef_, index=X_treino.columns).sort_values(key=abs, ascending=False)
print(coef.head(10))
print("intercepto:", linear.intercept_)
```

Leitura: o coeficiente indica a variação esperada no alvo quando aquela
característica aumenta em 1 unidade, **mantendo as demais constantes** — e
mesmo assim é associação, não causa.

## Resposta escrita — modelo pronto

> É um problema de **regressão**, porque a variável-alvo
> (`taxa_engajamento_pct`) é numérica e contínua: o objetivo é estimar um
> valor, não atribuir uma categoria (classificação) nem descobrir grupos sem
> rótulo (clusterização). O **MAE** mede o erro médio absoluto entre o valor
> previsto e o observado, na mesma unidade da taxa — quanto menor, mais
> próxima a estimativa. Escolhi **[MODELO]**, que apresentou o menor MAE no
> conjunto de teste. Uma limitação é que o modelo capta apenas associações
> estatísticas entre as características disponíveis antes da publicação e o
> engajamento observado nesta base; fatores não medidos (conteúdo da peça,
> contexto da data, distribuição do algoritmo da plataforma) podem explicar o
> resultado, então a previsão não deve ser lida como relação causal.

## Armadilhas

- **R² negativo não é bug.** Reporte e comente que o modelo tem baixo poder
  preditivo com as variáveis disponíveis — isso é uma conclusão legítima.
- Não avalie no treino. Métrica sempre em `X_teste`/`y_teste`.
- Árvore com `max_depth` alto decora o treino e vai mal no teste; o enunciado
  fixa `max_depth=4` justamente pra evitar isso.
- Se aparecer erro de texto não convertido → faltou `get_dummies`.
- Se aparecer erro de `NaN` → `df = df.dropna(subset=FEATURES + [ALVO])` antes.

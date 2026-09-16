# 00 — COLA RÁPIDA

Tudo que mais se usa, em uma página. Detalhe e explicação estão nos arquivos
numerados; aqui é só pra copiar rápido. 🔧 = trocar pelo nome real.

## Imports (cole no topo do notebook)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from sklearn.metrics import (
    mean_absolute_error, r2_score,
    precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay, silhouette_score,
)

pd.set_option("display.max_columns", None)
```

## Conhecer a base

```python
df = pd.read_csv("dados/ARQUIVO.csv")          # 🔧
df.head()                                       # 5 primeiras linhas
df.shape                                        # (linhas, colunas)
df.dtypes                                       # tipos
a = df.isna().sum(); a[a > 0]                   # só colunas com ausência
df["COL"].unique()                              # ver grafias inconsistentes
df["COL"].value_counts(dropna=False)            # contagem por categoria
df.duplicated(subset="ID").sum()                # nº de duplicatas
df.describe()                                   # estatísticas numéricas
```

## Limpeza

```python
df = df.drop_duplicates(subset="ID").copy()                      # 🔧
df["CAT"] = df["CAT"].str.strip().str.lower().str.title()        # padroniza texto
df["NUM"] = pd.to_numeric(df["NUM"], errors="coerce")            # texto → número

# ⚠️ DATA EM FORMATOS MISTOS — use duas passadas (ver 02-limpeza.md)
iso = pd.to_datetime(df["DATA"], errors="coerce", format="%Y-%m-%d")
br  = pd.to_datetime(df["DATA"], errors="coerce", format="%d/%m/%Y")
df["DATA"] = iso.fillna(br)

df = df.dropna(subset=["COL_ESSENCIAL"])                         # descartar
df["COL"] = df["COL"].fillna(df["COL"].median())                 # preencher
df = df[df["alcance"] > 0]                                       # inválidos
```

## Coluna calculada e tabela por grupo

```python
df["taxa"] = (df["A"] + df["B"]) / df["C"] * 100                 # 🔧 fórmula do enunciado

resumo = (df.groupby("CAT")["taxa"]
          .agg(publicacoes="count", mediana="median")
          .sort_values("mediana", ascending=False))

resumo2 = (df.groupby(["CAT_A", "CAT_B"])["taxa"]
           .agg(publicacoes="count", mediana="median")
           .sort_values("mediana", ascending=False)
           .reset_index())
```

## Gráficos (sempre: título + eixos + fonte)

```python
FONTE = "Fonte: dados sintéticos do Festival ViraBairro (2026)"   # 🔧
def fonte(): plt.figtext(0.5, -0.05, FONTE, ha="center", fontsize=9, style="italic")

# barras
plt.figure(figsize=(8,5)); plt.bar(resumo.index, resumo["mediana"], color="#4C72B0")
plt.title("TÍTULO"); plt.xlabel("X"); plt.ylabel("Y"); fonte(); plt.tight_layout(); plt.show()

# linha
plt.figure(figsize=(9,5)); plt.plot(serie.index, serie.values, marker="o")
plt.xticks(rotation=45, ha="right"); plt.title("T"); plt.xlabel("Dia"); plt.ylabel("Y")
fonte(); plt.tight_layout(); plt.show()

# barras horizontais (importâncias)
top = imp.head(5).sort_values()
plt.figure(figsize=(8,5)); plt.barh(top.index, top.values); plt.title("T"); plt.xlabel("Importância")
plt.tight_layout(); plt.show()

# dispersão real x previsto
plt.figure(figsize=(6,6)); plt.scatter(y_teste, y_prev, alpha=.6)
lo, hi = min(y_teste.min(), y_prev.min()), max(y_teste.max(), y_prev.max())
plt.plot([lo,hi],[lo,hi],"--",color="gray"); plt.xlabel("Real"); plt.ylabel("Previsto")
plt.tight_layout(); plt.show()
```

## Datas e recortes

```python
df["dia"] = df["DATA"].dt.date
diario = (df.groupby("dia")
          .agg(publicacoes=("ID","count"), media=("taxa","mean"), alcance_total=("alcance","sum"))
          .sort_index())

rec = df[(df["formato"] == "reel") & (df["hora"] >= 18)]
rec.nlargest(5, "taxa")[["ID","dia","hora","tema","taxa"]]
```

## Features sem vazamento (padrão do simulado)

```python
FEATURES = ["tema","formato","seguidores_autor","videos_autor","tamanho_legenda",
            "n_emojis","n_hashtags","hora","dia_semana","duracao_segundos"]   # 🔧
X = pd.get_dummies(df[FEATURES], columns=["tema","formato"], drop_first=True, dtype=int)
```

## Regressão (prever número)

```python
y = df["taxa_engajamento_pct"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)

lin = LinearRegression().fit(Xtr, ytr)
arv = DecisionTreeRegressor(max_depth=4, random_state=42).fit(Xtr, ytr)

tab = pd.DataFrame([{"modelo": n,
                     "MAE": mean_absolute_error(yte, m.predict(Xte)),
                     "R2":  r2_score(yte, m.predict(Xte))}
                    for n, m in [("Regressão linear", lin), ("Árvore de regressão", arv)]])
```

## Classificação (prever categoria)

```python
limite = df["taxa_engajamento_pct"].quantile(0.75)
y = (df["taxa_engajamento_pct"] > limite).astype(int)

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

modelos = {
  "Regressão logística": make_pipeline(StandardScaler(),
        LogisticRegression(max_iter=1000, class_weight="balanced")),
  "Árvore de classificação": DecisionTreeClassifier(max_depth=4, random_state=42, class_weight="balanced"),
  "Random Forest": RandomForestClassifier(random_state=42, class_weight="balanced"),
}
for m in modelos.values(): m.fit(Xtr, ytr)

tab = pd.DataFrame([{"modelo": n,
                     "precisao": precision_score(yte, m.predict(Xte), zero_division=0),
                     "recall":   recall_score(yte, m.predict(Xte), zero_division=0),
                     "f1":       f1_score(yte, m.predict(Xte), zero_division=0)}
                    for n, m in modelos.items()]).sort_values("f1", ascending=False)

melhor = modelos[tab.iloc[0]["modelo"]]
ConfusionMatrixDisplay(confusion_matrix(yte, melhor.predict(Xte)),
                       display_labels=["Não","Sim"]).plot()

# cortes
prob = modelos["Regressão logística"].predict_proba(Xte)[:, 1]
pd.DataFrame([{"corte": c,
               "precisao": precision_score(yte, (prob>=c).astype(int), zero_division=0),
               "recall":   recall_score(yte, (prob>=c).astype(int), zero_division=0),
               "f1":       f1_score(yte, (prob>=c).astype(int), zero_division=0)}
              for c in [0.50, 0.30]])

# importâncias (só árvore/floresta)
imp = pd.Series(arvore.feature_importances_, index=Xtr.columns).sort_values(ascending=False)
```

## Clusterização (agrupar sem rótulo)

```python
cols = ["seguidores_autor","tamanho_legenda","n_hashtags","taxa_engajamento_pct"]   # 🔧
base = df[cols].dropna()
Xs = StandardScaler().fit_transform(base)                    # escalonar é obrigatório

for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(Xs)
    print(k, km.inertia_, silhouette_score(Xs, km.labels_))

km = KMeans(n_clusters=3, random_state=42, n_init=10).fit(Xs)
base = base.copy(); base["cluster"] = km.labels_
base.groupby("cluster").mean().round(2)
```

## As 3 palavras-chave da resposta escrita

- **"associado a"**, nunca "causa".
- **"mediana"** = valor típico, menos sensível a extremos que a média.
- **"limitação"**: base sintética, período curto, poucos registros por grupo.

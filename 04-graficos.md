# 04 — Gráficos

**Regra que vale para todos:** título + nome dos dois eixos + **a fonte
escrita dentro da figura**. Se o enunciado escreve `Fonte: ...`, isso precisa
aparecer no gráfico, não só no texto da resposta.

## Bloco de abertura (cole uma vez por notebook)

```python
import matplotlib.pyplot as plt

FONTE = "Fonte: dados sintéticos do Festival ViraBairro (2026)"   # 🔧

def fonte():
    plt.figtext(0.5, -0.05, FONTE, ha="center", fontsize=9, style="italic")
```

Se a fonte sumir na hora de salvar/exportar, use uma alternativa que fica
dentro da área do gráfico:
```python
plt.xlabel(f"Tema\n{FONTE}")     # ou
plt.figtext(0.99, 0.01, FONTE, ha="right", fontsize=8, style="italic")
```

---

## Barras — comparar categorias

```python
resumo = df.groupby("tema")["taxa_utilidade_pct"].median().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(resumo.index, resumo.values, color="#4C72B0")
plt.title("Qual tema tem maior mediana de utilidade?")       # 🔧 comunique a PERGUNTA
plt.xlabel("Tema")                                            # 🔧
plt.ylabel("Mediana da taxa de utilidade (%)")                # 🔧
fonte()
plt.tight_layout()
plt.show()
```

Se `resumo` for um DataFrame (veio do `.agg`), use `resumo["mediana"]` no
lugar de `resumo.values`.

### Barras para combinação de duas categorias

```python
resumo2 = resumo2.copy()
resumo2["rotulo"] = resumo2["tema"] + " – " + resumo2["formato"]

plt.figure(figsize=(11, 6))
plt.bar(resumo2["rotulo"], resumo2["mediana"], color="#55A868")
plt.title("Mediana da taxa de engajamento por tema e formato")
plt.xlabel("Combinação tema × formato")
plt.ylabel("Mediana da taxa de engajamento (%)")
plt.xticks(rotation=45, ha="right")    # essencial: 16 rótulos não cabem retos
fonte()
plt.tight_layout()
plt.show()
```

### Barras agrupadas (uma cor por formato) — opcional, impressiona

```python
tabela = df.pivot_table(index="tema", columns="formato",
                        values="taxa_engajamento_pct", aggfunc="median")
tabela.plot(kind="bar", figsize=(10, 6))
plt.title("Mediana da taxa de engajamento por tema e formato")
plt.xlabel("Tema"); plt.ylabel("Mediana (%)")
plt.legend(title="Formato"); plt.xticks(rotation=0)
fonte(); plt.tight_layout(); plt.show()
```

## Barras horizontais — importância de variável

```python
top5 = importancias.head(5).sort_values()   # crescente: o maior fica no topo

plt.figure(figsize=(8, 5))
plt.barh(top5.index, top5.values, color="#C44E52")
plt.title("Características mais usadas pela árvore")
plt.xlabel("Importância")
plt.ylabel("Característica")
plt.tight_layout()
plt.show()
```

⚠️ Em `barh`, ordene **crescente** — o matplotlib desenha de baixo pra cima,
então `sort_values()` (crescente) deixa a maior barra no topo.

## Linha — evolução no tempo

```python
plt.figure(figsize=(9, 5))
plt.plot(diario.index, diario["engajamento_medio"], marker="o", color="#4C72B0")
plt.title("Taxa média de engajamento por dia")
plt.xlabel("Dia")
plt.ylabel("Taxa média de engajamento (%)")
plt.xticks(rotation=45, ha="right")
fonte()
plt.tight_layout()
plt.show()
```

`marker="o"` mostra onde há observação de verdade — importante quando há
poucos dias, pra não sugerir continuidade que não existe.

## Dispersão — real × previsto

```python
plt.figure(figsize=(6, 6))
plt.scatter(y_teste, y_previsto, alpha=0.6, color="#4C72B0")

lo = min(y_teste.min(), y_previsto.min())
hi = max(y_teste.max(), y_previsto.max())
plt.plot([lo, hi], [lo, hi], "--", color="gray", label="previsão = valor real")

plt.title("Valores reais vs. previstos — taxa de engajamento")
plt.xlabel("Valor real (%)")
plt.ylabel("Valor previsto (%)")
plt.legend()
plt.tight_layout()
plt.show()
```

A linha tracejada é a referência "acertou exatamente". Pontos acima dela =
modelo superestimou; abaixo = subestimou.

## Dispersão — relação entre duas variáveis

```python
plt.figure(figsize=(7, 5))
plt.scatter(df["tamanho_legenda"], df["taxa_engajamento_pct"], alpha=0.5)
plt.title("Tamanho da legenda e taxa de engajamento")
plt.xlabel("Tamanho da legenda (caracteres)")
plt.ylabel("Taxa de engajamento (%)")
fonte(); plt.tight_layout(); plt.show()
```

## Matriz de confusão

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_teste, previsto)
ConfusionMatrixDisplay(cm, display_labels=["Não", "Sim"]).plot(cmap="Blues")
plt.title("Matriz de confusão — Random Forest")   # 🔧 nome do modelo
plt.show()
```

## Armadilhas

- **Sempre `plt.figure()` antes** de cada gráfico novo, senão ele desenha em
  cima do anterior.
- `plt.show()` no final de cada um, senão eles se misturam.
- `plt.tight_layout()` evita rótulo cortado.
- Rótulos sobrepostos → `plt.xticks(rotation=45, ha="right")`.
- Título deve **comunicar a pergunta** quando o enunciado pedir isso —
  "Qual tema é mais salvo/compartilhado?" é melhor que "Taxa por tema".
- Não invente eixo truncado nem ordem aleatória: ordene por valor e comece o
  eixo Y em zero em gráfico de barras (é o padrão, só não mexa).

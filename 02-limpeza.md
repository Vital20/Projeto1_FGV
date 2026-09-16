# 02 — Limpeza e tratamento

**Quando usar:** base "suja" (`*_brutas.csv`) — duplicata, grafia
inconsistente, tipo errado, ausência, valor inválido, coluna calculada.

## Ordem recomendada

1. duplicata → 2. padronizar texto → 3. converter tipos → 4. tratar
ausência/inválido → 5. criar coluna calculada → 6. **conferir**

Faça nessa ordem: converter tipo antes de tirar duplicata desperdiça trabalho,
e criar a taxa antes de tratar o denominador gera `inf`.

---

## 1. Remover duplicata

```python
df = df.drop_duplicates(subset="id_publicacao").copy()   # 🔧 coluna identificadora
```

O `.copy()` no final evita o aviso `SettingWithCopyWarning` nas edições
seguintes. Sempre que você filtrar/fatiar e depois for **escrever** no
resultado, use `.copy()`.

Para conferir: `print(f"{antes} → {len(df)} linhas")`.

## 2. Padronizar texto categórico

Problema: `"Saúde"`, `"saúde"`, `" SAÚDE "` contam como quatro temas
diferentes no `groupby`.

```python
df["tema"] = df["tema"].str.strip().str.lower().str.title()
print(sorted(df["tema"].unique()))   # SEMPRE confira depois
```

- `.str.strip()` tira espaço nas pontas
- `.str.lower()` uniformiza a caixa
- `.str.title()` deixa "Saúde", "Mobilidade" (Primeira Maiúscula)

Se sobrarem grafias que não são só caixa/espaço (abreviação, erro de digitação,
sinônimo), corrija explicitamente:

```python
df["tema"] = df["tema"].replace({"Saude": "Saúde", "Mob.": "Mobilidade"})
```

🔧 **Nunca adivinhe o mapa** — rode `df["tema"].unique()` primeiro e escreva o
dicionário com base no que apareceu de verdade.

## 3. Converter tipos

### Números que vieram como texto

```python
for col in ["compartilhamentos", "salvamentos", "alcance"]:   # 🔧
    df[col] = pd.to_numeric(df[col], errors="coerce")
```

`errors="coerce"` faz o que não converte virar `NaN` em vez de quebrar o
código — aí você trata na etapa 4, de forma visível e justificada.

### ⚠️ Datas em formatos diferentes — a armadilha nº 1

O simulado diz explicitamente que há "datas em formatos distintos"
(`2026-08-05` misturado com `25/08/2026`). **O jeito óbvio dá errado sem dar
erro.** Testado:

| O que você escreve | O que acontece |
|---|---|
| `pd.to_datetime(s, errors="coerce")` | as datas `dd/mm/yyyy` viram **NaT** — você perde linhas silenciosamente |
| `pd.to_datetime(s, format="mixed", dayfirst=True)` | 🚨 **corrompe as ISO**: `2026-08-05` vira **8 de maio** |
| `pd.to_datetime(s, format="mixed")` | as `dd/mm` com dia ≤ 12 viram mês/dia (ex: `09/08` vira 8 de setembro) |
| **duas passadas por formato** ✅ | **tudo certo, zero perda** |

**A forma correta:**

```python
iso = pd.to_datetime(df["data_publicacao"], errors="coerce", format="%Y-%m-%d")
br  = pd.to_datetime(df["data_publicacao"], errors="coerce", format="%d/%m/%Y")
df["data_publicacao"] = iso.fillna(br)
```

Cada passada converte só o formato que ela entende e devolve `NaT` no resto;
o `fillna` junta os dois. Se houver um terceiro formato, é só mais uma linha.

**Confira sempre depois de converter:**

```python
print("não convertidas:", df["data_publicacao"].isna().sum())
print(df["data_publicacao"].min(), "→", df["data_publicacao"].max())
```

Se o intervalo não bate com o período que o enunciado descreve (ex: aparece
janeiro numa campanha de agosto-setembro), a conversão está errada.

Códigos de formato: `%Y` ano 4 dígitos · `%y` 2 dígitos · `%m` mês · `%d` dia
· `%H:%M` hora.

## 4. Tratar ausências e inválidos

Não existe resposta única — o que vale ponto é **justificar**. Padrões aceitos:

```python
# A) descartar: a coluna é essencial e não dá pra estimar
df = df.dropna(subset=["alcance"])

# B) preencher com mediana: manter a linha, sem inventar valor extremo
df["compartilhamentos"] = df["compartilhamentos"].fillna(df["compartilhamentos"].median())

# C) inválido que não é NaN (denominador zero/negativo)
df = df[df["alcance"] > 0].copy()
```

Regra prática:
- coluna que entra no **denominador** de uma taxa → descarte (A e C)
- coluna que entra na **soma** do numerador → preencher com mediana (B) é
  defensável, descartar também é
- **nunca** preencha com média quando houver outliers claros; a mediana é a
  escolha segura e mais fácil de justificar

⚠️ Não use `fillna(0)` em contagem sem pensar: zero é uma afirmação forte
("essa publicação teve zero compartilhamentos"), diferente de "não sabemos".

## 5. Criar coluna calculada

```python
df["taxa_utilidade_pct"] = (
    (df["compartilhamentos"] + df["salvamentos"]) / df["alcance"] * 100
)
```

🔧 A fórmula muda a cada prova — monte exatamente como está no enunciado.
Cuidado com a ordem: **some o numerador dentro de parênteses**, divida, e só
então multiplique por 100.

Se o denominador puder ser 0, você já tratou na etapa 4. Se não tratou, o
resultado vira `inf` (não é `NaN`, e não aparece em `isna()`):

```python
print(np.isinf(df["taxa_utilidade_pct"]).sum())
```

## 6. Conferir (10 segundos que salvam a questão)

```python
print(df.shape)
print(sorted(df["tema"].unique()))
print(df.dtypes)
print(df["taxa_utilidade_pct"].describe())
```

Taxa negativa, acima de 100%, ou `inf` = algo está errado no tratamento.

---

## Resposta escrita típica (decisões de tratamento)

Uma frase por decisão cobre o pedido:

> Removi registros duplicados por `id_publicacao` para não contar a mesma
> publicação duas vezes. Padronizei `tema` (espaços e caixa) porque a mesma
> categoria aparecia escrita de formas diferentes, o que dividiria os grupos.
> Converti as datas tratando separadamente os dois formatos presentes, para
> não perder nem inverter registros. Descartei linhas com `alcance` ausente ou
> não positivo, já que sem esse valor a taxa não pode ser calculada, e
> preenchi ausências de `compartilhamentos` e `salvamentos` com a mediana, por
> ser menos sensível a valores extremos que a média.

# 🎯 Guia de Consulta — Extração e Análise de Dados

Material de consulta para a prova (consulta ao GitHub liberada).
Organizado por **técnica**, não por questão — serve mesmo que a prova mude o
tema, os nomes das colunas ou a ordem das perguntas.

> ✅ **Todo o código deste repositório foi executado e testado** contra uma base
> sintética com o mesmo esquema de colunas do simulado (incluindo os defeitos
> propositais: grafia inconsistente, datas em formatos diferentes, duplicata,
> ausências e valores inválidos). O que está aqui roda.

---

## ⏱️ Roteiro de 30 segundos (faça isso em toda questão)

1. **Que arquivo?** `*_brutas.csv` → precisa limpar. `*_analise.csv` → usar direto.
2. **Que tipo de tarefa?** Olhe a tabela abaixo e abra **um** arquivo.
3. **Copie o bloco**, troque o que está marcado com 🔧 (nome de coluna, caminho, parâmetro).
4. **Rode e confira o resultado** — não confie que deu certo só porque não deu erro
   (ver `11-erros-comuns.md`, seção "erros que não dão erro").
5. **Resposta escrita?** Pegue a frase pronta em `10-frases-prontas.md` e adapte.
6. **Antes de fechar a questão**, bata o olho na lista dela em
   `12-erros-por-questao.md` — é a checagem mais rápida contra ponto perdido.

---

## 🔍 Índice: "o enunciado pede isso" → "abre esse arquivo"

| O enunciado pede... | Arquivo |
|---|---|
| head, shape, ausências, tipos, valores únicos, "conhecer a base" | `01-diagnostico.md` |
| tirar duplicata, padronizar texto, converter data/número, tratar ausência, criar coluna com fórmula | `02-limpeza.md` |
| tabela por grupo, contagem + média/mediana, cruzar duas categorias | `03-agrupar-e-tabelas.md` |
| gráfico de barras / linha / dispersão / horizontal, título, eixos, fonte | `04-graficos.md` |
| converter data, "por dia", recorte por hora/formato, top 5 | `05-datas-e-recortes.md` |
| **prever um número** (taxa esperada, alcance esperado) | `06-regressao.md` |
| **prever uma categoria** (merece/não merece), precisão, recall, F1, matriz de confusão, corte | `07-classificacao.md` |
| **agrupar sem rótulo**, KMeans, escolher k, perfis de grupo | `08-clusterizacao.md` |
| requests, BeautifulSoup, API, salvar em CSV/SQLite | `09-scraping-e-apis.md` |
| a **resposta escrita** em Markdown (causalidade, limitação, interpretação) | `10-frases-prontas.md` |
| deu erro / resultado estranho | `11-erros-comuns.md` |
| **conferir uma questão antes de fechar** ("o que dá pra errar na Q5?") | `12-erros-por-questao.md` |
| só quero o snippet, rápido | `00-COLA-RAPIDA.md` |

**Notebooks:**
- `notebook-consulta.ipynb` — todos os templates em células prontas pra copiar.
- `solucao-simulado-virabairro.ipynb` — o simulado inteiro resolvido e comentado.

💡 **Dica de velocidade:** no GitHub, aperte `t` para busca de arquivo ou use
`Ctrl+F` dentro do arquivo. Os títulos das seções usam as palavras do enunciado
("mediana por tema", "matriz de confusão", "vazamento") de propósito.

---

## ✅ Checklist — as 10 coisas que mais custam nota

1. **Recarregue o CSV** quando o enunciado disser "em uma nova variável". Não
   reaproveite um `df` já limpo de outra questão.
2. **Gráfico sem título / sem nome de eixo / sem a fonte escrita dentro da
   figura** é ponto perdido. Se o enunciado escreve "Fonte: ...", isso tem que
   aparecer no gráfico, não só no texto.
3. **Mediana ≠ média.** Se pediu mediana, use `median()`.
4. **Nunca afirme causalidade.** Use "associado a", "tende a", "nos dados
   observados". Nunca "causa", "prova que", "garante".
5. **Vazamento de dados:** para prever algo *antes* da publicação, não use
   `alcance`, `interacoes`, `compartilhamentos`, `salvamentos`, nem nada
   calculado a partir do alvo. Só o que existe antes de publicar.
6. **`random_state=42`** em tudo que sorteia (split, árvore, floresta, KMeans).
7. **`stratify=y`** no split de classificação; **escalone** (`StandardScaler`)
   antes de regressão logística e de KMeans.
8. **Categoria vira número** com `pd.get_dummies(..., drop_first=True, dtype=int)`
   antes de qualquer modelo — o scikit-learn não aceita texto.
9. **Confira depois de converter.** Datas em formatos misturados são a
   armadilha nº 1 do simulado: o jeito "óbvio" corrompe as datas **sem dar
   erro**. Veja `02-limpeza.md`, seção "⚠️ datas em formatos diferentes".
10. **Respeite o limite de frases** da resposta escrita. Responda exatamente o
    que foi pedido (indicação + explicação + limitação), sem enrolar.

---

## 📦 Estrutura

```
.
├── README.md                          ← você está aqui
├── 00-COLA-RAPIDA.md                  ← one-pager, os snippets mais usados
├── 01-diagnostico.md
├── 02-limpeza.md
├── 03-agrupar-e-tabelas.md
├── 04-graficos.md
├── 05-datas-e-recortes.md
├── 06-regressao.md
├── 07-classificacao.md
├── 08-clusterizacao.md
├── 09-scraping-e-apis.md
├── 10-frases-prontas.md
├── 11-erros-comuns.md
├── 12-erros-por-questao.md
├── notebook-consulta.ipynb
└── solucao-simulado-virabairro.ipynb
```

## 🚀 Subir no GitHub

```bash
cd consulta-simulado
git init
git add .
git commit -m "guia de consulta para a prova"
git branch -M main
git remote add origin https://github.com/BeAmara1/prova-pestana.git
git push -u origin main
```

Se o repositório já tiver algum arquivo (README criado pelo GitHub, por
exemplo), rode antes do push:
```bash
git pull origin main --allow-unrelated-histories
```

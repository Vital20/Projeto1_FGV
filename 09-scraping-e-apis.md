# 09 — Scraping, APIs e persistência

**Aviso:** o simulado ViraBairro diz explicitamente que *não* há coleta,
requisições web nem scraping. Este arquivo é **seguro de reserva**, caso a
prova real cobre as aulas 08 (BeautifulSoup), 09 (Playwright) ou 14 (API e
persistência). Se a sua prova for só de análise, pule.

## Requisições com `requests`

```python
import requests

url = "https://exemplo.com/pagina"          # 🔧
resposta = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})

print(resposta.status_code)                  # 200 = ok, 404 = não existe, 403 = bloqueado
html = resposta.text
```

Boas práticas que valem ponto: `timeout`, checar `status_code`, `User-Agent`,
e **pausa entre requisições** (`time.sleep(1)`) para não sobrecarregar o site.

## Extrair com BeautifulSoup

```python
from bs4 import BeautifulSoup

sopa = BeautifulSoup(html, "html.parser")

sopa.find("h1").get_text(strip=True)                 # primeiro elemento
sopa.find_all("a")                                   # todos
sopa.find("div", class_="card")                      # por classe (note o _)
sopa.select("div.card h2")                           # seletor CSS
sopa.find("a")["href"]                               # atributo
```

Coleta em laço, o padrão mais cobrado:

```python
linhas = []
for card in sopa.select("div.card"):                 # 🔧 seletor do site
    linhas.append({
        "titulo": card.select_one("h2").get_text(strip=True),
        "data":   card.select_one(".data").get_text(strip=True),
        "link":   card.select_one("a")["href"],
    })

df = pd.DataFrame(linhas)
```

⚠️ Proteja contra elemento ausente, senão um `None` quebra o laço inteiro:
```python
el = card.select_one("h2")
titulo = el.get_text(strip=True) if el else None
```

### Tabela pronta em HTML

```python
tabelas = pd.read_html(html)      # lista de DataFrames
df = tabelas[0]
```

## Páginas dinâmicas (Playwright)

Use quando o conteúdo só aparece depois do JavaScript rodar (o `requests`
devolve a página "vazia").

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    pagina = navegador.new_page()
    pagina.goto("https://exemplo.com")            # 🔧
    pagina.wait_for_selector("div.card")          # espera carregar
    html = pagina.content()
    navegador.close()
```

Rolagem infinita:
```python
for _ in range(5):
    pagina.mouse.wheel(0, 5000)
    pagina.wait_for_timeout(1500)
```

## Consumir API pública

```python
resposta = requests.get("https://api.exemplo.com/dados",
                        params={"cidade": "Rio", "limite": 100},
                        timeout=20)
resposta.raise_for_status()
dados = resposta.json()

df = pd.DataFrame(dados)                        # se vier lista de objetos
df = pd.json_normalize(dados["resultados"])     # se vier aninhado
```

Paginação:
```python
todos = []
for pagina_num in range(1, 6):
    r = requests.get(url, params={"page": pagina_num}, timeout=20)
    if r.status_code != 200:
        break
    todos.extend(r.json()["dados"])
    time.sleep(1)
df = pd.DataFrame(todos)
```

## Persistência

```python
# CSV
df.to_csv("dados/resultado.csv", index=False)
df = pd.read_csv("dados/resultado.csv")

# Parquet (mais leve, preserva tipos)
df.to_parquet("dados/resultado.parquet")

# SQLite
import sqlite3
con = sqlite3.connect("dados/base.db")
df.to_sql("publicacoes", con, if_exists="replace", index=False)
df = pd.read_sql("SELECT * FROM publicacoes WHERE tema = 'Cultura'", con)
con.close()

# DuckDB
import duckdb
duckdb.sql("SELECT tema, median(taxa) FROM df GROUP BY tema").df()
```

`index=False` no `to_csv` evita criar uma coluna extra sem nome — erro comum.

## Ética e limites (cai na resposta escrita)

> A coleta respeitou o `robots.txt` e usou intervalo entre requisições para
> não sobrecarregar o servidor. Os dados coletados refletem apenas o que
> estava publicamente disponível no momento da coleta, em um recorte
> específico de páginas, e podem mudar a qualquer momento — o que limita a
> reprodutibilidade e impede generalizar os resultados para toda a
> plataforma.

Pontos que valem ponto: `robots.txt`, termos de uso, dados pessoais,
intervalo entre requisições, **pipeline reexecutável** (mesmo script roda de
novo e reproduz o resultado), registro da data de coleta.

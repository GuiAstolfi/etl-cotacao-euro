# 💶 ETL Cotação Euro — Dashboard em Tempo Real

Projeto de **Engenharia de Dados** que implementa um pipeline ETL completo para coleta, transformação e visualização da cotação do Euro (EUR/BRL) em tempo real.

> Desenvolvido para demonstrar habilidades práticas em construção de pipelines de dados, integração com APIs REST e visualização de dados.

---

## 📸 Visão Geral

O projeto segue a arquitetura clássica de um pipeline de dados moderno:

**API REST → Extração → Transformação → Banco de Dados → Dashboard**

- **`pipeline.py`** → Pipeline ETL que consome a API, transforma e persiste os dados automaticamente
- **`dashboard.py`** → Dashboard interativo com métricas e gráficos atualizados em tempo real

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| `Python` | Linguagem principal |
| `Requests` | Consumo da API de cotações |
| `Pandas` | Transformação dos dados |
| `SQLAlchemy` | Conexão com o banco de dados |
| `SQLite` | Armazenamento local dos dados |
| `Streamlit` | Interface do dashboard |
| `Plotly` | Gráficos interativos |

---

## 📁 Estrutura do Projeto

```
etl-cotacao-euro/
│
├── pipeline.py          # ETL: extração, transformação e carga
├── dashboard.py         # Dashboard Streamlit
├── requirements.txt     # Dependências do projeto
└── README.md
```

---

## 🔌 API Utilizada

[AwesomeAPI — Economia](https://economia.awesomeapi.com.br/)

Endpoint usado:
```
GET https://economia.awesomeapi.com.br/last/EUR-BRL
```

---

## 📊 Funcionalidades do Dashboard

- 📋 Tabela com histórico das cotações
- 💰 Valor máximo registado
- 📉 Valor mínimo registado
- 📈 Gráfico de evolução do preço do Euro
- 🔄 Botão de atualização manual

---

## 🧠 Competências Demonstradas

- Consumo de **APIs REST** com Python
- Construção de pipeline **ETL** com separação clara de responsabilidades
- Modelagem e persistência de dados com **SQLite + SQLAlchemy**
- Visualização de dados com **Plotly** e **Streamlit**
- Automação de coleta de dados com loop contínuo

---

## 👤 Autor

Feito por **Guilherme Astolfi**  
🔗 [github.com/GuiAstolfi](https://github.com/GuiAstolfi)

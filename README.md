# 🚀 Crypto-Pipeline: Coleta, Processamento e Entrega Automatizada com Telegram

## 🌟 Visão Geral do Projeto

Este projeto demonstra a construção de uma **pipeline completa e modular de dados**, desenvolvida em Python, para coletar cotações de criptomoedas em tempo real (via CoinGecko API) e entregar resultados formatados por meio de um **Telegram Bot**.

O foco da arquitetura foi a **Programação Orientada a Objetos (POO)** e a **Composição** para garantir código limpo, testável e de fácil manutenção, simulando um ambiente de trabalho de engenharia de software real.

---

## 💻 Habilidades Técnicas em Destaque

Este projeto prova o domínio das seguintes competências essenciais para engenheiros de software e analistas de dados:

| Categoria | Habilidade Demonstrada |
| :--- | :--- |
| **Arquitetura & POO** | Criação de uma hierarquia de classes (Herança e Abstração) com `BaseCollector` e `CoinCollector`. Uso de **Composição** para orquestrar a pipeline (`Collector` + `Processor`). |
| **Processamento de Dados** | Utilização da biblioteca **Pandas** para manipulação, limpeza e transformação de dados brutos (cálculo de variação, formatação numérica, filtragem de colunas). |
| **Integração (APIs)** | Consumo robusto de APIs RESTful utilizando a biblioteca `requests`, incluindo tratamento de erros e gestão de *timeouts*. |
| **Automação & Entrega** | Implementação de um **Bot Telegram** como camada de interface (UI) usando `python-telegram-bot`, garantindo a entrega do valor de negócio ao usuário final. |

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.10+
* **Gestão de Ambientes:** Conda
* **Bibliotecas Principais:**
    * `requests`: Requisições HTTP robustas.
    * `pandas`: Limpeza e manipulação de dados.
    * `python-telegram-bot`: Interface de comunicação.

## ⚙️ Arquitetura Modular (POO e Composição)

O projeto é dividido em módulos claros, que se comunicam para formar a pipeline (Design Pattern: *Pipeline*):

1.  **`BasePipeline.py`**: Define a interface abstrata (`BaseCollector`) utilizando o módulo `abc`.
2.  **`CoinCollector.py`**: Implementa a coleta, lidando com a API da CoinGecko e o tratamento de erros (Módulo 1).
3.  **`DataProcessor.py`**: Recebe os dados brutos, aplica a lógica de negócio (renomear colunas, calcular variação com emojis, formatar preços) e retorna um `DataFrame` limpo (Módulo 2).
4.  **`TelegramBot.py` (Orquestrador)**: Gerencia os comandos do bot, orquestra a chamada dos Módulos 1 e 2, monta a mensagem final e a envia ao usuário (Módulo 3).

---

## 💡 Como Executar o Projeto

### 1. Configuração do Ambiente

```bash
# Crie o ambiente Conda
conda create -n crypto-pipeline python=3.13

# Ative o ambiente
conda activate crypto-pipeline

# Instale as dependências (Priorizando Conda, usando pip para o Bot)
conda install pandas requests
pip install python-telegram-bot



# 🏠 Zillow Property Scraper & Google Form Automation

Este projeto realiza **web scraping** de propriedades de um site clone do Zillow e envia automaticamente os dados (endereço, preço e link) para um **formulário do Google Forms** usando **Python, BeautifulSoup e Selenium**.

## 🚀 Funcionalidades

- Extrai os dados de:
  - Endereço da propriedade
  - Preço mensal
  - Link para mais informações
- Preenche automaticamente um formulário do Google Forms com esses dados
- Automatiza o envio de múltiplas entradas para o formulário

## 📌 Tecnologias utilizadas

- `requests` — para fazer a requisição HTTP à página web
- `BeautifulSoup` — para fazer o parsing e extração dos dados HTML
- `Selenium` — para automação do navegador e envio dos dados ao formulário

## 🛠️ Pré-requisitos

- Python 3.7 ou superior
- Google Chrome instalado
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) compatível com a versão do seu navegador
- Instalar os pacotes necessários:

```bash
pip install requests beautifulsoup4 selenium


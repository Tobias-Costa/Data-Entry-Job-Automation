import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Cabeçalhos para simular um navegador real e evitar bloqueio do site
headers = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}

# Faz uma requisição HTTP para a página simulada do Zillow
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=headers)
response.raise_for_status()

# Converte o conteúdo HTML em texto
contents = response.text

# Cria um objeto BeautifulSoup para fazer parsing do HTML
soup = BeautifulSoup(contents, "html.parser")

# Seleciona todos os cards de propriedades
all_homes = soup.select("div .StyledPropertyCardDataWrapper")

# Extrai os endereços das propriedades
home_address = [
    home.find("address").get_text().replace(" | ", " ").strip()
    for home in all_homes
]

# Extrai os preços das propriedades
home_prices = [
    home.find("span", class_="PropertyCardWrapper__StyledPriceLine")
    .get_text()
    .replace("/mo", "")
    .split("+")[0]
    for home in all_homes
]

# Extrai os links das propriedades
home_links = [
    home.find("a", class_="StyledPropertyCardDataArea-anchor")["href"]
    for home in all_homes
]

# Inicia o navegador do Selenium (Chrome)
driver = webdriver.Chrome()

# Abre o formulário do Google Forms
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfbNZxbADc3oNW-IvErNluBkuYUUC1Xo7nT_Ys49bDJvax0Ow/viewform?usp=dialog")
time.sleep(3)  # Aguarda o carregamento completo da página

# Itera sobre todos os imóveis coletados
for i in range(len(home_address)):

    # Preenche o campo de endereço
    address_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    # Preenche o campo de preço
    price_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    # Preenche o campo de link
    link_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # Botão de envio
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    # Envia os dados para o formulário
    address_field.send_keys(home_address[i])
    price_field.send_keys(home_prices[i])
    link_field.send_keys(home_links[i])
    time.sleep(1)
    submit_button.click()
    time.sleep(2)

    # Clica em "Enviar outra resposta"
    send_another_response_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another_response_button.click()
    time.sleep(2)

# Fecha o navegador após preencher todos os dados
driver.quit()

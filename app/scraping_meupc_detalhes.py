from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Função para coletar detalhes de um produto
def coletar_detalhes_produto(driver, url):
    driver.get(url)
    time.sleep(4)
    try:
        nome = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    except:
        nome = ''
    try:
        preco = driver.find_element(By.XPATH, "//*[contains(text(),'R$')]").text.strip()
    except:
        preco = ''
    try:
        img = driver.find_element(By.TAG_NAME, 'img').get_attribute('src')
    except:
        img = ''
    try:
        especs = driver.find_element(By.TAG_NAME, 'main').text.strip()
    except:
        especs = ''
    return {'nome': nome, 'preco': preco, 'especificacoes': especs, 'imagem': img, 'url': url}

# Carregar os links dos produtos já coletados
with open('processadores_meupc.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    produtos = list(reader)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

detalhes = []
for prod in produtos:
    detalhes.append(coletar_detalhes_produto(driver, prod['url']))
    print(f"Coletado: {prod['nome']}")

driver.quit()

with open('processadores_meupc_detalhado.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['nome', 'preco', 'especificacoes', 'imagem', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in detalhes:
        writer.writerow(row)

print(f'{len(detalhes)} processadores detalhados salvos em processadores_meupc_detalhado.csv')

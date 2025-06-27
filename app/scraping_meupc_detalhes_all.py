from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import os

CATEGORIAS = {
    'placas_mae': 'https://meupc.net/placas-mae',
    'memoria_ram': 'https://meupc.net/memorias',
    'placa_de_video': 'https://meupc.net/placas-video',
    'fonte': 'https://meupc.net/fontes',
    'gabinete': 'https://meupc.net/gabinetes',
    'armazenamento': 'https://meupc.net/armazenamentos',
}

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

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

def coletar_categoria(nome_cat, url):
    print(f'Coletando {nome_cat}...')
    driver.get(url)
    time.sleep(7)
    data = []
    links = driver.find_elements(By.XPATH, "//a[contains(@href, '/peca/')]")
    for link in links:
        nome = link.text.strip()
        href = link.get_attribute('href')
        if nome:
            data.append({'nome': nome, 'url': href})
    detalhes = []
    for prod in data:
        detalhes.append(coletar_detalhes_produto(driver, prod['url']))
        print(f"Coletado: {prod['nome']}")
    with open(f'{nome_cat}_meupc_detalhado.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['nome', 'preco', 'especificacoes', 'imagem', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in detalhes:
            writer.writerow(row)
    print(f'{len(detalhes)} produtos detalhados salvos em {nome_cat}_meupc_detalhado.csv')
    return len(detalhes)

total = 0
for cat, url in CATEGORIAS.items():
    total += coletar_categoria(cat, url)

driver.quit()
print(f'Total geral: {total} produtos detalhados coletados.')

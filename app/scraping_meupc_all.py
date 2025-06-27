from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

CATEGORIAS = {
    'processadores': 'https://meupc.net/processadores',
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
    with open(f'{nome_cat}_meupc.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['nome', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f'{len(data)} produtos coletados em {nome_cat}_meupc.csv')
    return len(data)

total = 0
for cat, url in CATEGORIAS.items():
    total += coletar_categoria(cat, url)

driver.quit()
print(f'Total geral: {total} produtos coletados.')

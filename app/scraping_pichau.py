import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# URLs das categorias na Pichau
CATEGORIAS = {
    'processadores': 'https://www.pichau.com.br/hardware/processadores',
    'placas_mae': 'https://www.pichau.com.br/hardware/placas-mae',
    'memorias_ram': 'https://www.pichau.com.br/hardware/memorias',
    'armazenamento': 'https://www.pichau.com.br/hardware/armazenamento',
    'placas_de_video': 'https://www.pichau.com.br/hardware/placas-de-video',
    'fontes': 'https://www.pichau.com.br/hardware/fontes',
    'gabinetes': 'https://www.pichau.com.br/hardware/gabinetes',
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def get_produtos_categoria(url, max_pages=2):
    produtos = []
    for page in range(1, max_pages+1):
        pag_url = f"{url}?page={page}"
        resp = requests.get(pag_url, headers=HEADERS)
        soup = BeautifulSoup(resp.text, 'html.parser')
        # Novo seletor para cards de produto
        cards = soup.select('a.sc-6b3c1a84-0')
        for card in cards:
            nome = card.select_one('h2.sc-6b3c1a84-4')
            preco = card.select_one('div.sc-d6a30908-2 span')
            link = card.get('href')
            if nome and preco and link:
                produto_url = 'https://www.pichau.com.br' + link
                especificacoes = get_especificacoes(produto_url)
                produtos.append({
                    'nome': nome.text.strip(),
                    'preco': preco.text.strip(),
                    'url': produto_url,
                    **especificacoes
                })
        time.sleep(1)
    return produtos

def get_produtos_categoria_selenium(url, max_pages=2):
    produtos = []
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    for page in range(1, max_pages+1):
        pag_url = f"{url}?page={page}"
        driver.get(pag_url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards = soup.select('a.sc-6b3c1a84-0')
        for card in cards:
            nome = card.select_one('h2.sc-6b3c1a84-4')
            preco = card.select_one('div.sc-d6a30908-2 span')
            link = card.get('href')
            if nome and preco and link:
                produto_url = 'https://www.pichau.com.br' + link
                especificacoes = get_especificacoes(produto_url)
                produtos.append({
                    'nome': nome.text.strip(),
                    'preco': preco.text.strip(),
                    'url': produto_url,
                    **especificacoes
                })
    driver.quit()
    return produtos

def get_especificacoes(url):
    resp = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')
    especs = {}
    tabela = soup.find('table')
    if tabela:
        for row in tabela.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) == 2:
                chave = cols[0].text.strip()
                valor = cols[1].text.strip()
                especs[chave] = valor
    return especs

def main():
    for categoria, url in CATEGORIAS.items():
        print(f'Coletando {categoria}...')
        produtos = get_produtos_categoria_selenium(url)
        df = pd.DataFrame(produtos)
        df.to_csv(f'{categoria}_pichau.csv', index=False)
        print(f'{len(produtos)} produtos salvos em {categoria}_pichau.csv')

if __name__ == '__main__':
    main()

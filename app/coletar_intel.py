import requests
from bs4 import BeautifulSoup
import pandas as pd

# Exemplo: Coleta de processadores Intel do site ARK
BASE_URL = "https://ark.intel.com"
LISTA_URL = "https://ark.intel.com/content/www/br/pt/ark/products/series/1250/10th-generation-intel-core-i7-processors.html"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def get_lista_processadores():
    resp = requests.get(LISTA_URL, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = soup.select('a.ark-product-name')
    produtos = []
    for link in links[:10]:  # Limite para exemplo
        nome = link.text.strip()
        url = BASE_URL + link['href']
        print(f"Coletando: {nome}")
        especificacoes, imagem = get_detalhes_processador(url)
        produtos.append({
            'nome': nome,
            'url': url,
            'imagem': imagem,
            **especificacoes
        })
    return produtos

def get_detalhes_processador(url):
    resp = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')
    especs = {}
    # Especificações
    for row in soup.select('tr.spec-row'):
        cols = row.find_all('td')
        if len(cols) == 2:
            chave = cols[0].text.strip()
            valor = cols[1].text.strip()
            especs[chave] = valor
    # Imagem
    img_tag = soup.select_one('img.ark-product-image')
    imagem = img_tag['src'] if img_tag else ''
    return especs, imagem

def main():
    produtos = get_lista_processadores()
    df = pd.DataFrame(produtos)
    df.to_csv('processadores_intel.csv', index=False)
    print(f'{len(produtos)} processadores salvos em processadores_intel.csv')

if __name__ == '__main__':
    main()

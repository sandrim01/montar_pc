import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://meupc.net/processadores'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')

# Exemplo de estrutura, pode ser necessário ajustar conforme o HTML real
data = []
for card in soup.find_all('div', class_='product-card'):
    nome = card.find('h2').get_text(strip=True) if card.find('h2') else ''
    preco = card.find('span', class_='price').get_text(strip=True) if card.find('span', class_='price') else ''
    especificacoes = card.find('ul', class_='specs')
    especificacoes_texto = especificacoes.get_text(' | ', strip=True) if especificacoes else ''
    imagem = card.find('img')['src'] if card.find('img') else ''
    data.append({
        'nome': nome,
        'preco': preco,
        'especificacoes': especificacoes_texto,
        'imagem': imagem
    })

with open('processadores_meupc.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['nome', 'preco', 'especificacoes', 'imagem']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f'{len(data)} processadores coletados e salvos em processadores_meupc.csv')

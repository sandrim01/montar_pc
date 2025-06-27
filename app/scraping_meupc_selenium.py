from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

url = 'https://meupc.net/processadores'

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
time.sleep(7)

data = []
links = driver.find_elements(By.XPATH, "//a[contains(@href, '/peca/')]")
for link in links:
    nome = link.text.strip()
    href = link.get_attribute('href')
    if nome and 'processador' in nome.lower():
        data.append({'nome': nome, 'url': href})

driver.quit()

with open('processadores_meupc.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['nome', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f'{len(data)} processadores coletados e salvos em processadores_meupc.csv')

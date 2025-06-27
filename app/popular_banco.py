import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

produtos = {
    'processadores': [
        ("Intel Core i9-14900K", 3999.90, "LGA1700"),
        ("AMD Ryzen 9 7950X", 3699.00, "AM5"),
        ("Intel Core i5-13400F", 1199.00, "LGA1700"),
        ("AMD Ryzen 5 7600X", 1299.00, "AM5")
    ],
    'placas_mae': [
        ("ASUS ROG Strix Z790-E", 2499.00, "LGA1700", "DDR5"),
        ("Gigabyte B650M DS3H", 899.00, "AM5", "DDR5"),
        ("ASRock B450M Steel Legend", 599.00, "AM4", "DDR4")
    ],
    'memorias_ram': [
        ("Corsair Vengeance 16GB DDR5", 499.00, "DDR5"),
        ("Kingston Fury 16GB DDR4", 299.00, "DDR4")
    ],
    'armazenamentos': [
        ("Samsung 970 EVO Plus 1TB", 499.00, "SSD NVMe"),
        ("Seagate Barracuda 2TB", 399.00, "HDD")
    ],
    'placas_video': [
        ("NVIDIA GeForce RTX 4070 Ti", 4999.00),
        ("AMD Radeon RX 7800 XT", 3999.00)
    ],
    'fontes': [
        ("Corsair RM750x", 699.00, "750W"),
        ("PCYES Electro V2 600W", 299.00, "600W")
    ],
    'gabinetes': [
        ("NZXT H510", 499.00),
        ("Cooler Master MasterBox Q300L", 299.00)
    ],
    'monitores': [
        ("LG UltraGear 27GL850", 1799.00, "27", "2560x1440"),
        ("Samsung Odyssey G5", 1499.00, "27", "2560x1440")
    ],
    'teclados': [
        ("Logitech G Pro X", 699.00, "Mecânico"),
        ("Redragon Kumara K552", 199.00, "Mecânico")
    ],
    'mouses': [
        ("Logitech G502 Hero", 299.00, "Óptico"),
        ("Razer DeathAdder V2", 349.00, "Óptico")
    ],
    'headsets': [
        ("HyperX Cloud II", 499.00),
        ("Logitech G733", 799.00)
    ],
    'caixas_som': [
        ("Logitech Z313", 249.00),
        ("Edifier R1000T4", 399.00)
    ],
    'webcams': [
        ("Logitech C920", 399.00),
        ("Razer Kiyo", 599.00)
    ],
    'estabilizadores': [
        ("SMS Progressive III 1200VA", 399.00, "Eletrônico"),
        ("Ragtech Easy Way 600VA", 199.00, "Eletrônico")
    ],
    'impressoras': [
        ("HP Ink Tank 416", 899.00, "Tanque de tinta"),
        ("Epson EcoTank L3250", 1199.00, "Tanque de tinta")
    ],
    'acessorios': [
        ("Base para notebook Multilaser", 59.00, "Suporte"),
        ("Hub USB 3.0 Orico", 89.00, "Hub USB")
    ]
}

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

# Inserção dos produtos
cur.execute('DELETE FROM processadores')
cur.execute('DELETE FROM placas_mae')
cur.execute('DELETE FROM memorias_ram')
cur.execute('DELETE FROM armazenamentos')
cur.execute('DELETE FROM placas_video')
cur.execute('DELETE FROM fontes')
cur.execute('DELETE FROM gabinetes')
cur.execute('DELETE FROM monitores')
cur.execute('DELETE FROM teclados')
cur.execute('DELETE FROM mouses')
cur.execute('DELETE FROM headsets')
cur.execute('DELETE FROM caixas_som')
cur.execute('DELETE FROM webcams')
cur.execute('DELETE FROM estabilizadores')
cur.execute('DELETE FROM impressoras')
cur.execute('DELETE FROM acessorios')

cur.executemany('INSERT INTO processadores (nome, preco, soquete) VALUES (%s, %s, %s)', produtos['processadores'])
cur.executemany('INSERT INTO placas_mae (nome, preco, soquete, ram) VALUES (%s, %s, %s, %s)', produtos['placas_mae'])
cur.executemany('INSERT INTO memorias_ram (nome, preco, tipo) VALUES (%s, %s, %s)', produtos['memorias_ram'])
cur.executemany('INSERT INTO armazenamentos (nome, preco, tipo) VALUES (%s, %s, %s)', produtos['armazenamentos'])
cur.executemany('INSERT INTO placas_video (nome, preco) VALUES (%s, %s)', produtos['placas_video'])
cur.executemany('INSERT INTO fontes (nome, preco, potencia) VALUES (%s, %s, %s)', produtos['fontes'])
cur.executemany('INSERT INTO gabinetes (nome, preco) VALUES (%s, %s)', produtos['gabinetes'])
cur.executemany('INSERT INTO monitores (nome, preco, tamanho, resolucao) VALUES (%s, %s, %s, %s)', produtos['monitores'])
cur.executemany('INSERT INTO teclados (nome, preco, tipo) VALUES (%s, %s, %s)', produtos['teclados'])
cur.executemany('INSERT INTO mouses (nome, preco, tipo) VALUES (%s, %s, %s)', produtos['mouses'])
cur.executemany('INSERT INTO headsets (nome, preco) VALUES (%s, %s)', produtos['headsets'])
cur.executemany('INSERT INTO caixas_som (nome, preco) VALUES (%s, %s)', produtos['caixas_som'])
cur.executemany('INSERT INTO webcams (nome, preco) VALUES (%s, %s)', produtos['webcams'])
cur.executemany('INSERT INTO estabilizadores (nome, preco, tipo) VALUES (%s, %s, %s)', produtos['estabilizadores'])
cur.executemany('INSERT INTO impressoras (nome, preco, tipo) VALUES (%s, %s, %s)', produtos['impressoras'])
cur.executemany('INSERT INTO acessorios (nome, preco, categoria) VALUES (%s, %s, %s)', produtos['acessorios'])

conn.commit()
cur.close()
conn.close()
print('Produtos inseridos com sucesso!')

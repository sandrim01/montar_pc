import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

# Exemplo de processadores detalhados
processadores = [
    ("Intel Core i9-14900K", 3999.90, "Intel", "i9-14900K", "LGA1700", 24, 32, 3.2, 6.0, 125, "14ª Geração", "Intel UHD 770"),
    ("Intel Core i7-13700K", 2699.90, "Intel", "i7-13700K", "LGA1700", 16, 24, 3.4, 5.4, 125, "13ª Geração", "Intel UHD 770"),
    ("AMD Ryzen 9 7950X", 3699.00, "AMD", "7950X", "AM5", 16, 32, 4.5, 5.7, 170, "Zen 4", "Não possui"),
    ("AMD Ryzen 7 7800X3D", 2499.00, "AMD", "7800X3D", "AM5", 8, 16, 4.2, 5.0, 120, "Zen 4", "Não possui"),
    ("Intel Core i5-13400F", 1199.00, "Intel", "i5-13400F", "LGA1700", 10, 16, 2.5, 4.6, 65, "13ª Geração", "Não possui"),
    ("AMD Ryzen 5 5600G", 899.00, "AMD", "5600G", "AM4", 6, 12, 3.9, 4.4, 65, "Zen 3", "Radeon Vega 7")
]

cur.execute('DELETE FROM processadores')
cur.executemany('''INSERT INTO processadores (nome, preco, marca, modelo, soquete, nucleos, threads, frequencia_base, frequencia_turbo, tdp, geracao, graficos_integrados) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', processadores)

# Exemplo de placas-mãe detalhadas
placas_mae = [
    ("ASUS ROG Strix Z790-E", 2499.00, "ASUS", "ROG Strix Z790-E", "LGA1700", "Z790", "DDR5", 128, 4, 4, 6, 3, True, True),
    ("Gigabyte B650M DS3H", 899.00, "Gigabyte", "B650M DS3H", "AM5", "B650", "DDR5", 128, 4, 2, 4, 2, False, False),
    ("ASRock B450M Steel Legend", 599.00, "ASRock", "B450M Steel Legend", "AM4", "B450", "DDR4", 64, 4, 1, 4, 1, False, False)
]
cur.execute('DELETE FROM placas_mae')
cur.executemany('''INSERT INTO placas_mae (nome, preco, marca, modelo, soquete, chipset, ram, max_ram, slots_ram, m2_slots, sata_ports, pci_slots, wifi, bluetooth) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', placas_mae)

# Exemplo de memórias RAM detalhadas
memorias_ram = [
    ("Corsair Vengeance 16GB DDR5 6000MHz", 499.00, "Corsair", "Vengeance", "DDR5", 16, 6000, "36"),
    ("Kingston Fury 16GB DDR4 3200MHz", 299.00, "Kingston", "Fury", "DDR4", 16, 3200, "16")
]
cur.execute('DELETE FROM memorias_ram')
cur.executemany('''INSERT INTO memorias_ram (nome, preco, marca, modelo, tipo, capacidade, frequencia, latencia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''', memorias_ram)

# Exemplo de armazenamentos detalhados
armazenamentos = [
    ("Samsung 970 EVO Plus 1TB", 499.00, "Samsung", "970 EVO Plus", "SSD NVMe", 1000, "NVMe", 3500, 3300),
    ("Seagate Barracuda 2TB", 399.00, "Seagate", "Barracuda", "HDD", 2000, "SATA", 220, 220)
]
cur.execute('DELETE FROM armazenamentos')
cur.executemany('''INSERT INTO armazenamentos (nome, preco, marca, modelo, tipo, capacidade, interface, leitura, gravacao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''', armazenamentos)

# Exemplo de placas de vídeo detalhadas
placas_video = [
    ("NVIDIA GeForce RTX 4070 Ti", 4999.00, "NVIDIA", "RTX 4070 Ti", 12, "GDDR6X", 285, 2310, 2610),
    ("AMD Radeon RX 7800 XT", 3999.00, "AMD", "RX 7800 XT", 16, "GDDR6", 263, 2124, 2430)
]
cur.execute('DELETE FROM placas_video')
cur.executemany('''INSERT INTO placas_video (nome, preco, marca, modelo, vram, tipo_vram, tdp, clock_base, clock_turbo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''', placas_video)

# Exemplo de fontes detalhadas
fontes = [
    ("Corsair RM750x", 699.00, "Corsair", "RM750x", "750W", "80 Plus Gold", True),
    ("PCYES Electro V2 600W", 299.00, "PCYES", "Electro V2", "600W", "80 Plus White", False)
]
cur.execute('DELETE FROM fontes')
cur.executemany('''INSERT INTO fontes (nome, preco, marca, modelo, potencia, certificacao, modular) VALUES (%s,%s,%s,%s,%s,%s,%s)''', fontes)

# Exemplo de gabinetes detalhados
gabinetes = [
    ("NZXT H510", 499.00, "NZXT", "H510", "Mid Tower", 2, 2),
    ("Cooler Master MasterBox Q300L", 299.00, "Cooler Master", "MasterBox Q300L", "Micro ATX", 2, 1)
]
cur.execute('DELETE FROM gabinetes')
cur.executemany('''INSERT INTO gabinetes (nome, preco, marca, modelo, formato, baias, fans_inclusos) VALUES (%s,%s,%s,%s,%s,%s,%s)''', gabinetes)

conn.commit()
cur.close()
conn.close()
print('Produtos detalhados inseridos com sucesso!')

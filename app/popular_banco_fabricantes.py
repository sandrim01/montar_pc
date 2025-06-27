import psycopg2
from datetime import date

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

# Exemplo detalhado de processadores
processadores = [
    ("Intel Core i9-14900K", 3999.90, "Intel", "i9-14900K", "LGA1700", 24, 32, 3.2, 6.0, 125, "14ª Geração", "Intel UHD 770", "10nm", 36, "5.0", "DDR5-5600/DDR4-3200", "SSE4.1, SSE4.2, AVX2, AVX-512", date(2023,10,17)),
    ("AMD Ryzen 9 7950X", 3699.00, "AMD", "7950X", "AM5", 16, 32, 4.5, 5.7, 170, "Zen 4", "Não possui", "5nm", 64, "5.0", "DDR5-5200", "SSE4a, AVX2, FMA3, SHA", date(2022,9,27)),
    ("Intel Core i5-13400F", 1199.00, "Intel", "i5-13400F", "LGA1700", 10, 16, 2.5, 4.6, 65, "13ª Geração", "Não possui", "10nm", 20, "4.0", "DDR5-4800/DDR4-3200", "SSE4.1, SSE4.2, AVX2", date(2023,1,3)),
    ("AMD Ryzen 5 5600G", 899.00, "AMD", "5600G", "AM4", 6, 12, 3.9, 4.4, 65, "Zen 3", "Radeon Vega 7", "7nm", 16, "3.0", "DDR4-3200", "SSE4a, AVX2, FMA3", date(2021,4,13))
]
cur.execute('DELETE FROM processadores')
cur.executemany('''INSERT INTO processadores (nome, preco, marca, modelo, soquete, nucleos, threads, frequencia_base, frequencia_turbo, tdp, geracao, graficos_integrados, litografia, cache_l3, pcie, suporte_memoria, instrucoes, data_lancamento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', processadores)

# Exemplo detalhado de placas-mãe
placas_mae = [
    ("ASUS ROG Strix Z790-E", 2499.00, "LGA1700", "DDR5", "ASUS", "ROG Strix Z790-E", "Z790", 128, 4, 4, 6, 3, True, True, "ATX", "ROG SupremeFX", "2.5G LAN", "USB 3.2 Gen2x2, USB-C", True, "UEFI BIOS", True),
    ("Gigabyte B650M DS3H", 899.00, "AM5", "DDR5", "Gigabyte", "B650M DS3H", "B650", 128, 4, 2, 4, 2, False, False, "Micro ATX", "Realtek ALC897", "1G LAN", "USB 3.2 Gen1", False, "UEFI BIOS", False)
]
cur.execute('DELETE FROM placas_mae')
cur.executemany('''INSERT INTO placas_mae (nome, preco, soquete, ram, marca, modelo, chipset, max_ram, slots_ram, m2_slots, sata_ports, pci_slots, wifi, bluetooth, formato, audio, lan, usb_ports, rgb, bios, overclock) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', placas_mae)

# Exemplo detalhado de memórias RAM
memorias_ram = [
    ("Corsair Vengeance 16GB DDR5 6000MHz", 499.00, "Corsair", "Vengeance", "DDR5", 16, 6000, "36", False, True, True, 1.35),
    ("Kingston Fury 16GB DDR4 3200MHz", 299.00, "Kingston", "Fury", "DDR4", 16, 3200, "16", False, True, True, 1.2)
]
cur.execute('DELETE FROM memorias_ram')
cur.executemany('''INSERT INTO memorias_ram (nome, preco, marca, modelo, tipo, capacidade, frequencia, latencia, ecc, xmp, dissipador, voltagem) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', memorias_ram)

# Exemplo detalhado de armazenamentos
armazenamentos = [
    ("Samsung 970 EVO Plus 1TB", 499.00, "Samsung", "970 EVO Plus", "SSD NVMe", 1000, "NVMe", 3500, 3300, "V-NAND 3-bit MLC", True, 600, 1500000, "80x22x2.3mm"),
    ("Seagate Barracuda 2TB", 399.00, "Seagate", "Barracuda", "HDD", 2000, "SATA", 220, 220, "CMR", False, 180, 1000000, "147x101x20mm")
]
cur.execute('DELETE FROM armazenamentos')
cur.executemany('''INSERT INTO armazenamentos (nome, preco, marca, modelo, tipo, capacidade, interface, leitura, gravacao, nand, dram, tbw, mtbf, dimensoes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', armazenamentos)

# Exemplo detalhado de placas de vídeo
placas_video = [
    ("NVIDIA GeForce RTX 4070 Ti", 4999.00, "NVIDIA", "RTX 4070 Ti", 12, "GDDR6X", 285, 2310, 2610, "3x DisplayPort, 1x HDMI", True, True, 7680),
    ("AMD Radeon RX 7800 XT", 3999.00, "AMD", "RX 7800 XT", 16, "GDDR6", 263, 2124, 2430, "2x DisplayPort, 1x HDMI", True, False, 3840)
]
cur.execute('DELETE FROM placas_video')
cur.executemany('''INSERT INTO placas_video (nome, preco, marca, modelo, vram, tipo_vram, tdp, clock_base, clock_turbo, conectores, ray_tracing, dlss, cuda_cores) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', placas_video)

# Exemplo detalhado de fontes
fontes = [
    ("Corsair RM750x", 699.00, "Corsair", "RM750x", "750W", "80 Plus Gold", True, "Ativo", "OCP, OVP, UVP, SCP, OTP", 90.0, "24-pin ATX, 2x EPS, 4x PCIe", "160x150x86mm"),
    ("PCYES Electro V2 600W", 299.00, "PCYES", "Electro V2", "600W", "80 Plus White", False, "Ativo", "OCP, OVP, SCP", 85.0, "24-pin ATX, 1x EPS, 2x PCIe", "140x150x86mm")
]
cur.execute('DELETE FROM fontes')
cur.executemany('''INSERT INTO fontes (nome, preco, marca, modelo, potencia, certificacao, modular, pfc, protecoes, eficiencia, cabos, dimensoes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', fontes)

# Exemplo detalhado de gabinetes
gabinetes = [
    ("NZXT H510", 499.00, "NZXT", "H510", "Mid Tower", 2, 2, "Alto", True, True, 165),
    ("Cooler Master MasterBox Q300L", 299.00, "Cooler Master", "MasterBox Q300L", "Micro ATX", 2, 1, "Médio", True, False, 159)
]
cur.execute('DELETE FROM gabinetes')
cur.executemany('''INSERT INTO gabinetes (nome, preco, marca, modelo, formato, baias, fans_inclusos, airflow, filtros, suporte_watercooler, altura_max_cooler) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', gabinetes)

conn.commit()
cur.close()
conn.close()
print('Produtos detalhados dos fabricantes inseridos com sucesso!')

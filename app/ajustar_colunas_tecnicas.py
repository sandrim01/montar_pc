import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

# Adiciona colunas técnicas em processadores
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN marca VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN modelo VARCHAR(50);")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN nucleos INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN threads INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN frequencia_base DECIMAL(5,2);")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN frequencia_turbo DECIMAL(5,2);")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN tdp INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN geracao VARCHAR(20);")
except Exception: pass
try:
    cur.execute("ALTER TABLE processadores ADD COLUMN graficos_integrados VARCHAR(50);")
except Exception: pass

# Adiciona colunas técnicas em placas_mae
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN marca VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN modelo VARCHAR(50);")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN chipset VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN max_ram INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN slots_ram INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN m2_slots INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN sata_ports INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN pci_slots INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN wifi BOOLEAN;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_mae ADD COLUMN bluetooth BOOLEAN;")
except Exception: pass

# Adiciona colunas técnicas em memorias_ram
try:
    cur.execute("ALTER TABLE memorias_ram ADD COLUMN marca VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE memorias_ram ADD COLUMN modelo VARCHAR(50);")
except Exception: pass
try:
    cur.execute("ALTER TABLE memorias_ram ADD COLUMN capacidade INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE memorias_ram ADD COLUMN frequencia INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE memorias_ram ADD COLUMN latencia VARCHAR(10);")
except Exception: pass

# Adiciona colunas técnicas em armazenamentos
try:
    cur.execute("ALTER TABLE armazenamentos ADD COLUMN marca VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE armazenamentos ADD COLUMN modelo VARCHAR(50);")
except Exception: pass
try:
    cur.execute("ALTER TABLE armazenamentos ADD COLUMN capacidade INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE armazenamentos ADD COLUMN interface VARCHAR(20);")
except Exception: pass
try:
    cur.execute("ALTER TABLE armazenamentos ADD COLUMN leitura INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE armazenamentos ADD COLUMN gravacao INT;")
except Exception: pass

# Adiciona colunas técnicas em placas_video
try:
    cur.execute("ALTER TABLE placas_video ADD COLUMN marca VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_video ADD COLUMN modelo VARCHAR(50);")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_video ADD COLUMN vram INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_video ADD COLUMN tipo_vram VARCHAR(10);")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_video ADD COLUMN tdp INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_video ADD COLUMN clock_base INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE placas_video ADD COLUMN clock_turbo INT;")
except Exception: pass

# Adiciona colunas técnicas em fontes
try:
    cur.execute("ALTER TABLE fontes ADD COLUMN marca VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE fontes ADD COLUMN modelo VARCHAR(50);")
except Exception: pass
try:
    cur.execute("ALTER TABLE fontes ADD COLUMN certificacao VARCHAR(20);")
except Exception: pass
try:
    cur.execute("ALTER TABLE fontes ADD COLUMN modular BOOLEAN;")
except Exception: pass

# Adiciona colunas técnicas em gabinetes
try:
    cur.execute("ALTER TABLE gabinetes ADD COLUMN marca VARCHAR(30);")
except Exception: pass
try:
    cur.execute("ALTER TABLE gabinetes ADD COLUMN modelo VARCHAR(50);")
except Exception: pass
try:
    cur.execute("ALTER TABLE gabinetes ADD COLUMN formato VARCHAR(20);")
except Exception: pass
try:
    cur.execute("ALTER TABLE gabinetes ADD COLUMN baias INT;")
except Exception: pass
try:
    cur.execute("ALTER TABLE gabinetes ADD COLUMN fans_inclusos INT;")
except Exception: pass

conn.commit()
cur.close()
conn.close()
print('Colunas técnicas adicionadas com sucesso!')

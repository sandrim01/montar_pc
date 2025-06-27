import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

# Campos extras para processadores
def add_column(table, column, coltype):
    try:
        cur.execute(f"ALTER TABLE {table} ADD COLUMN {column} {coltype};")
    except Exception:
        pass

# Processadores
add_column('processadores', 'litografia', 'VARCHAR(20)')
add_column('processadores', 'cache_l3', 'INT')
add_column('processadores', 'pcie', 'VARCHAR(20)')
add_column('processadores', 'suporte_memoria', 'VARCHAR(50)')
add_column('processadores', 'instrucoes', 'TEXT')
add_column('processadores', 'data_lancamento', 'DATE')

# Placas-mãe
add_column('placas_mae', 'formato', 'VARCHAR(20)')
add_column('placas_mae', 'audio', 'VARCHAR(50)')
add_column('placas_mae', 'lan', 'VARCHAR(50)')
add_column('placas_mae', 'usb_ports', 'VARCHAR(50)')
add_column('placas_mae', 'rgb', 'BOOLEAN')
add_column('placas_mae', 'bios', 'VARCHAR(50)')
add_column('placas_mae', 'overclock', 'BOOLEAN')

# Memórias RAM
add_column('memorias_ram', 'ecc', 'BOOLEAN')
add_column('memorias_ram', 'xmp', 'BOOLEAN')
add_column('memorias_ram', 'dissipador', 'BOOLEAN')
add_column('memorias_ram', 'voltagem', 'DECIMAL(4,2)')

# Armazenamentos
add_column('armazenamentos', 'nand', 'VARCHAR(20)')
add_column('armazenamentos', 'dram', 'BOOLEAN')
add_column('armazenamentos', 'tbw', 'INT')
add_column('armazenamentos', 'mtbf', 'INT')
add_column('armazenamentos', 'dimensoes', 'VARCHAR(30)')

# Placas de vídeo
add_column('placas_video', 'conectores', 'VARCHAR(50)')
add_column('placas_video', 'ray_tracing', 'BOOLEAN')
add_column('placas_video', 'dlss', 'BOOLEAN')
add_column('placas_video', 'cuda_cores', 'INT')

# Fontes
add_column('fontes', 'pfc', 'VARCHAR(20)')
add_column('fontes', 'protecoes', 'VARCHAR(100)')
add_column('fontes', 'eficiencia', 'DECIMAL(4,2)')
add_column('fontes', 'cabos', 'TEXT')
add_column('fontes', 'dimensoes', 'VARCHAR(30)')

# Gabinetes
add_column('gabinetes', 'airflow', 'VARCHAR(30)')
add_column('gabinetes', 'filtros', 'BOOLEAN')
add_column('gabinetes', 'suporte_watercooler', 'BOOLEAN')
add_column('gabinetes', 'altura_max_cooler', 'INT')

conn.commit()
cur.close()
conn.close()
print('Colunas técnicas extras adicionadas com sucesso!')

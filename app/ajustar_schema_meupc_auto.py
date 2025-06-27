import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

# Ajustes necessários para garantir compatibilidade com importação automatizada
AJUSTES = [
    # memoria_ram
    ("memoria_ram", "preco", "NUMERIC", False),
    ("memoria_ram", "tipo", "VARCHAR(100)", False),
    ("memoria_ram", "url", "TEXT", False),
    ("memoria_ram", "imagem", "TEXT", False),
    ("memoria_ram", "especificacoes", "TEXT", False),
    # placa_de_video
    ("placa_de_video", "preco", "NUMERIC", False),
    ("placa_de_video", "url", "TEXT", False),
    ("placa_de_video", "imagem", "TEXT", False),
    ("placa_de_video", "especificacoes", "TEXT", False),
    # fonte
    ("fonte", "preco", "NUMERIC", False),
    ("fonte", "url", "TEXT", False),
    ("fonte", "imagem", "TEXT", False),
    ("fonte", "especificacoes", "TEXT", False),
    # gabinete
    ("gabinete", "preco", "NUMERIC", False),
    ("gabinete", "url", "TEXT", False),
    ("gabinete", "imagem", "TEXT", False),
    ("gabinete", "especificacoes", "TEXT", False),
    # armazenamento
    ("armazenamento", "preco", "NUMERIC", False),
    ("armazenamento", "url", "TEXT", False),
    ("armazenamento", "imagem", "TEXT", False),
    ("armazenamento", "especificacoes", "TEXT", False),
]

def ajustar_tabelas():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for tabela, coluna, tipo, notnull in AJUSTES:
        try:
            cur.execute(f"""
                ALTER TABLE {tabela} ADD COLUMN IF NOT EXISTS {coluna} {tipo};
            """)
            if notnull:
                cur.execute(f"ALTER TABLE {tabela} ALTER COLUMN {coluna} SET NOT NULL;")
            print(f"Coluna {coluna} da tabela {tabela} ajustada/criada como {tipo}")
        except Exception as e:
            print(f"Erro ao ajustar {coluna} em {tabela}: {e}")
            conn.rollback()
    conn.commit()
    cur.close()
    conn.close()
    print('Ajustes de schema concluídos.')

if __name__ == "__main__":
    ajustar_tabelas()

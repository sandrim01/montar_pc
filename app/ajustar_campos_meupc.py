import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

# Ajustar todos os campos 'nome' e outros relevantes para VARCHAR(150) ou mais
ALTERS = [
    ("placas_mae", "soquete", 100),
    ("placas_mae", "nome", 150),
    ("memoria_ram", "nome", 150),
    ("memoria_ram", "tipo", 100),
    ("processadores", "nome", 150),
    ("processadores", "soquete", 100),
    ("placa_de_video", "nome", 150),
    ("fonte", "nome", 150),
    ("gabinete", "nome", 150),
    ("armazenamento", "nome", 150),
]

def ajustar_campos():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for tabela, campo, tamanho in ALTERS:
        try:
            cur.execute(f"""
                ALTER TABLE {tabela}
                ALTER COLUMN {campo} TYPE VARCHAR({tamanho});
            """)
            print(f"Campo {campo} da tabela {tabela} ajustado para VARCHAR({tamanho})")
        except Exception as e:
            print(f"Erro ao ajustar {campo} em {tabela}: {e}")
            conn.rollback()
    conn.commit()
    cur.close()
    conn.close()
    print('Ajuste de campos concluído.')

if __name__ == "__main__":
    ajustar_campos()

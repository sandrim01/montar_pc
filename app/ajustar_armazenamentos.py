import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE armazenamentos ADD COLUMN tipo VARCHAR(20);")
    conn.commit()
    print("Coluna 'tipo' adicionada com sucesso em 'armazenamentos'.")
except Exception as e:
    print(f"Erro ou coluna já existe: {e}")
finally:
    cur.close()
    conn.close()

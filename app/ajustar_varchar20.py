import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

QUERY = '''
SELECT table_name, column_name
FROM information_schema.columns
WHERE data_type = 'character varying' AND character_maximum_length = 20
  AND table_schema = 'public';
'''

def ajustar_todos_varchar20():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute(QUERY)
    results = cur.fetchall()
    for table, column in results:
        try:
            cur.execute(f"ALTER TABLE {table} ALTER COLUMN {column} TYPE VARCHAR(150);")
            print(f"Campo {column} da tabela {table} ajustado para VARCHAR(150)")
        except Exception as e:
            print(f"Erro ao ajustar {column} em {table}: {e}")
            conn.rollback()
    conn.commit()
    cur.close()
    conn.close()
    print('Ajuste automático de todos os VARCHAR(20) concluído.')

if __name__ == "__main__":
    ajustar_todos_varchar20()

import psycopg2

# Configurações do banco de dados (dados fornecidos pelo usuário)
DB_HOST = 'maglev.proxy.rlwy.net'
DB_PORT = '52420'
DB_NAME = 'railway'
DB_USER = 'postgres'
DB_PASS = 'tlFQnkpHDYvruDCfMZWptHDIDTceUrVK'

# Tabelas e colunas a garantir
TABELAS = [
    'processadores',
    'placas_mae',
    'memoria_ram',
    'armazenamento',
    'placa_de_video',
    'fonte',
    'gabinete',
]
CAMPOS = [
    ('especificacoes', 'TEXT'),
    ('imagem', 'TEXT'),
    ('url', 'TEXT'),
]

def criar_tabela_se_nao_existir(cur, tabela):
    sql = f"""
    CREATE TABLE IF NOT EXISTS {tabela} (
        id SERIAL PRIMARY KEY
    );
    """
    cur.execute(sql)

def garantir_unique_nome(cur, tabela):
    # Tenta criar o índice UNIQUE na coluna nome
    try:
        cur.execute(f"ALTER TABLE {tabela} ADD CONSTRAINT {tabela}_nome_unique UNIQUE (nome);")
    except psycopg2.errors.DuplicateObject:
        pass
    except Exception as e:
        if 'already exists' not in str(e):
            print(f'Erro ao criar UNIQUE em {tabela}:', e)

def ajustar_schema():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()
    for tabela in TABELAS:
        criar_tabela_se_nao_existir(cur, tabela)
        for campo, tipo in CAMPOS:
            sql = f"""
            ALTER TABLE {tabela}
            ADD COLUMN IF NOT EXISTS {campo} {tipo};
            """
            cur.execute(sql)
        # Garante UNIQUE em nome
        try:
            cur.execute(f"ALTER TABLE {tabela} ADD COLUMN IF NOT EXISTS nome TEXT;")
        except Exception:
            pass
        garantir_unique_nome(cur, tabela)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    ajustar_schema()

import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

def criar_tabelas():
    comandos = [
        '''CREATE TABLE IF NOT EXISTS processadores (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            soquete VARCHAR(20) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS placas_mae (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            soquete VARCHAR(20) NOT NULL,
            ram VARCHAR(20) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS memorias_ram (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            tipo VARCHAR(20) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS armazenamentos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            tipo VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS placas_video (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS fontes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            potencia VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS gabinetes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS monitores (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            tamanho VARCHAR(20),
            resolucao VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS teclados (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            tipo VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS mouses (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            tipo VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS headsets (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS caixas_som (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS webcams (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS estabilizadores (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            tipo VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS impressoras (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            tipo VARCHAR(20)
        )''',
        '''CREATE TABLE IF NOT EXISTS acessorios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            categoria VARCHAR(50)
        )'''
    ]
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for comando in comandos:
        cur.execute(comando)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Tabelas criadas com sucesso!")

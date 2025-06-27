import psycopg2

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

def criar_tabelas():
    comandos = [
        '''CREATE TABLE IF NOT EXISTS processadores (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            marca VARCHAR(30) NOT NULL,
            modelo VARCHAR(50),
            soquete VARCHAR(20) NOT NULL,
            nucleos INT,
            threads INT,
            frequencia_base DECIMAL(5,2),
            frequencia_turbo DECIMAL(5,2),
            tdp INT,
            geracao VARCHAR(20),
            graficos_integrados VARCHAR(50)
        )''',
        '''CREATE TABLE IF NOT EXISTS placas_mae (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            marca VARCHAR(30),
            modelo VARCHAR(50),
            soquete VARCHAR(20) NOT NULL,
            chipset VARCHAR(30),
            ram VARCHAR(20) NOT NULL,
            max_ram INT,
            slots_ram INT,
            m2_slots INT,
            sata_ports INT,
            pci_slots INT,
            wifi BOOLEAN,
            bluetooth BOOLEAN
        )''',
        '''CREATE TABLE IF NOT EXISTS memorias_ram (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            marca VARCHAR(30),
            modelo VARCHAR(50),
            tipo VARCHAR(20) NOT NULL,
            capacidade INT,
            frequencia INT,
            latencia VARCHAR(10)
        )''',
        '''CREATE TABLE IF NOT EXISTS armazenamentos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            marca VARCHAR(30),
            modelo VARCHAR(50),
            tipo VARCHAR(20),
            capacidade INT,
            interface VARCHAR(20),
            leitura INT,
            gravacao INT
        )''',
        '''CREATE TABLE IF NOT EXISTS placas_video (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            marca VARCHAR(30),
            modelo VARCHAR(50),
            vram INT,
            tipo_vram VARCHAR(10),
            tdp INT,
            clock_base INT,
            clock_turbo INT
        )''',
        '''CREATE TABLE IF NOT EXISTS fontes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            marca VARCHAR(30),
            modelo VARCHAR(50),
            potencia VARCHAR(20),
            certificacao VARCHAR(20),
            modular BOOLEAN
        )''',
        '''CREATE TABLE IF NOT EXISTS gabinetes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10,2) NOT NULL,
            marca VARCHAR(30),
            modelo VARCHAR(50),
            formato VARCHAR(20),
            baias INT,
            fans_inclusos INT
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
    print("Tabelas detalhadas criadas com sucesso!")

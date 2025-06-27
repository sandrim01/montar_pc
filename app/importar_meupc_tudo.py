import psycopg2
import pandas as pd
import re

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"

# Funções utilitárias

def limpar_preco(preco):
    if not isinstance(preco, str):
        return 0.0
    match = re.search(r'R\$\s*([\d\.]+,\d{2})', preco)
    if match:
        valor = match.group(1).replace('.', '').replace(',', '.')
        try:
            return float(valor)
        except:
            return 0.0
    return 0.0

def extrair_soquete(especificacoes):
    if not isinstance(especificacoes, str):
        return ''
    for linha in especificacoes.split('\n'):
        if 'soquete' in linha.lower() or 'socket' in linha.lower():
            partes = linha.split(':')
            if len(partes) > 1:
                return partes[1].strip()
            else:
                return linha.strip()
    return 'desconhecido'

def extrair_tipo_memoria(especificacoes):
    if not isinstance(especificacoes, str):
        return ''
    for linha in especificacoes.split('\n'):
        if 'ddr' in linha.lower():
            return linha.strip()
    return 'desconhecido'

def extrair_ram(especificacoes):
    if not isinstance(especificacoes, str):
        return ''
    for linha in especificacoes.split('\n'):
        if 'ram' in linha.lower() or 'memória' in linha.lower():
            return linha.strip()
    return 'desconhecido'

def importar_placas_mae():
    df = pd.read_csv('placas_mae_meupc_detalhado.csv')
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = row.get('especificacoes', '')
        preco = limpar_preco(row.get('preco', ''))
        soquete = extrair_soquete(especificacoes)
        ram = extrair_ram(especificacoes)
        if not ram:
            ram = 'desconhecido'
        cur.execute(
            """
            INSERT INTO placas_mae (nome, preco, soquete, ram, url, imagem, especificacoes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET preco=EXCLUDED.preco, soquete=EXCLUDED.soquete, ram=EXCLUDED.ram, url=EXCLUDED.url, imagem=EXCLUDED.imagem, especificacoes=EXCLUDED.especificacoes
            """,
            (
                row.get('nome'),
                preco,
                soquete,
                ram,
                row.get('url'),
                row.get('imagem'),
                especificacoes
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Placas-mãe importadas/atualizadas com sucesso!')

def importar_memoria_ram():
    df = pd.read_csv('memoria_ram_meupc_detalhado.csv')
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = row.get('especificacoes', '')
        preco = limpar_preco(row.get('preco', ''))
        tipo = extrair_tipo_memoria(especificacoes)
        cur.execute(
            """
            INSERT INTO memoria_ram (nome, preco, tipo, url, imagem, especificacoes)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET preco=EXCLUDED.preco, tipo=EXCLUDED.tipo, url=EXCLUDED.url, imagem=EXCLUDED.imagem, especificacoes=EXCLUDED.especificacoes
            """,
            (
                row.get('nome'),
                preco,
                tipo,
                row.get('url'),
                row.get('imagem'),
                especificacoes
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Memórias RAM importadas/atualizadas com sucesso!')

def importar_placas_video():
    df = pd.read_csv('placa_de_video_meupc_detalhado.csv')
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = row.get('especificacoes', '')
        preco = limpar_preco(row.get('preco', ''))
        cur.execute(
            """
            INSERT INTO placa_de_video (nome, preco, url, imagem, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET preco=EXCLUDED.preco, url=EXCLUDED.url, imagem=EXCLUDED.imagem, especificacoes=EXCLUDED.especificacoes
            """,
            (
                row.get('nome'),
                preco,
                row.get('url'),
                row.get('imagem'),
                especificacoes
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Placas de vídeo importadas/atualizadas com sucesso!')

def importar_fontes():
    df = pd.read_csv('fonte_meupc_detalhado.csv')
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = row.get('especificacoes', '')
        preco = limpar_preco(row.get('preco', ''))
        cur.execute(
            """
            INSERT INTO fonte (nome, preco, url, imagem, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET preco=EXCLUDED.preco, url=EXCLUDED.url, imagem=EXCLUDED.imagem, especificacoes=EXCLUDED.especificacoes
            """,
            (
                row.get('nome'),
                preco,
                row.get('url'),
                row.get('imagem'),
                especificacoes
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Fontes importadas/atualizadas com sucesso!')

def importar_gabinetes():
    df = pd.read_csv('gabinete_meupc_detalhado.csv')
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = row.get('especificacoes', '')
        preco = limpar_preco(row.get('preco', ''))
        cur.execute(
            """
            INSERT INTO gabinete (nome, preco, url, imagem, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET preco=EXCLUDED.preco, url=EXCLUDED.url, imagem=EXCLUDED.imagem, especificacoes=EXCLUDED.especificacoes
            """,
            (
                row.get('nome'),
                preco,
                row.get('url'),
                row.get('imagem'),
                especificacoes
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Gabinetes importados/atualizados com sucesso!')

def importar_armazenamentos():
    df = pd.read_csv('armazenamento_meupc_detalhado.csv')
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = row.get('especificacoes', '')
        preco = limpar_preco(row.get('preco', ''))
        cur.execute(
            """
            INSERT INTO armazenamento (nome, preco, url, imagem, especificacoes)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET preco=EXCLUDED.preco, url=EXCLUDED.url, imagem=EXCLUDED.imagem, especificacoes=EXCLUDED.especificacoes
            """,
            (
                row.get('nome'),
                preco,
                row.get('url'),
                row.get('imagem'),
                especificacoes
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Armazenamentos importados/atualizados com sucesso!')

if __name__ == "__main__":
    importar_placas_mae()
    importar_memoria_ram()
    importar_placas_video()
    importar_fontes()
    importar_gabinetes()
    importar_armazenamentos()
    print('Importação de todas as categorias concluída!')

import psycopg2
import pandas as pd
import re

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"
CSV_PATH = "processadores_meupc_detalhado.csv"

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
    # Procura por linhas que contenham "Soquete" ou "Socket"
    for linha in especificacoes.split('\n'):
        if 'soquete' in linha.lower() or 'socket' in linha.lower():
            partes = linha.split(':')
            if len(partes) > 1:
                return partes[1].strip()
            else:
                return linha.strip()
    return ''

def importar_processadores():
    df = pd.read_csv(CSV_PATH)
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = row.get('especificacoes', '')
        preco = limpar_preco(row.get('preco', ''))
        soquete = extrair_soquete(especificacoes)
        if not soquete:
            soquete = 'desconhecido'
        cur.execute(
            """
            INSERT INTO processadores (nome, preco, soquete, url, imagem, especificacoes)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET preco=EXCLUDED.preco, soquete=EXCLUDED.soquete, url=EXCLUDED.url, imagem=EXCLUDED.imagem, especificacoes=EXCLUDED.especificacoes
            """,
            (
                row.get('nome'),
                preco,
                soquete,
                row.get('url'),
                row.get('imagem'),
                especificacoes
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Processadores do meupc.net importados/atualizados com sucesso!')

if __name__ == "__main__":
    importar_processadores()

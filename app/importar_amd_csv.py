import psycopg2
import pandas as pd

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"
CSV_PATH = r"c:/Users/mb/Downloads/Especificações de processadores.csv"

def importar_processadores_amd():
    df = pd.read_csv(CSV_PATH)
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        especificacoes = {k: row[k] for k in df.columns if k not in ['Nome','Soquete da CPU'] and pd.notnull(row[k])}
        cur.execute(
            """
            INSERT INTO processadores (nome, soquete, especificacoes)
            VALUES (%s, %s, %s)
            ON CONFLICT (nome) DO UPDATE SET soquete=EXCLUDED.soquete, especificacoes=EXCLUDED.especificacoes
            """,
            (
                str(row.get('Nome')),
                str(row.get('Soquete da CPU')),
                str(especificacoes)
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print('Processadores AMD importados/atualizados com sucesso!')

if __name__ == "__main__":
    importar_processadores_amd()

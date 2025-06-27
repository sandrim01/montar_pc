import psycopg2
import pandas as pd
import glob
import os

DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"
CATEGORIAS = [
    'processadores',
    'placas_mae',
    'memoria_ram',
    'placa_de_video',
    'fonte',
    'gabinete',
    'armazenamento',
]

def importar_categoria(categoria):
    csv_path = f"{categoria}_meupc.csv"
    if not os.path.exists(csv_path):
        print(f"Arquivo {csv_path} não encontrado.")
        return
    df = pd.read_csv(csv_path)
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute(
            f"""
            INSERT INTO {categoria} (nome, url)
            VALUES (%s, %s)
            ON CONFLICT (nome) DO UPDATE SET url=EXCLUDED.url
            """,
            (
                row.get('nome'),
                row.get('url')
            )
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f'{categoria} importados/atualizados com sucesso!')

if __name__ == "__main__":
    for cat in CATEGORIAS:
        importar_categoria(cat)

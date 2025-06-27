import psycopg2
DB_URL = "postgresql://postgres:tlFQnkpHDYvruDCfMZWptHDIDTceUrVK@maglev.proxy.rlwy.net:52420/railway"
conn = psycopg2.connect(DB_URL)
cur = conn.cursor()
cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'placas_mae' ORDER BY ordinal_position;")
for row in cur.fetchall():
    print(row[0])
cur.close()
conn.close()

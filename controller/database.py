import psycopg2

def connectDB():
  try:
    conn = psycopg2.connect(host = "localhost", user = "postgres", password = "123", dbname = "bila_cuci_montor")
    cur = conn.cursor()
    return conn,cur
  except Exception:
    return None

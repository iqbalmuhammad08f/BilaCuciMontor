import psycopg2

def connect():
  return psycopg2.connect(
    host = "localhost",
    database = "projectbasda",
    user = "postgres",
    password = "123"
  )

def tambahPenghuni(nama, umur):
  conn = connect()
  cur = conn.cursor()
  cur.execute("INSERT INTO penghuni_kos (nama,umur) VALUES(%s,%s)",(nama,umur))
  conn.commit()
  cur.close()
  conn.close()
  print("data berhasil ditambahkan")

def lihatPenghuni():
  conn = connect()
  cur = conn.cursor()
  cur.execute("SELECT * FROM penghuni_kos")
  rows = cur.fetchall()
  for row in rows:
    print(row)
  cur.close()
  conn.close()

def hapusPenghuni(nama):
  conn = connect()
  cur = conn.cursor()
  cur.execute("DELETE FROM penghuni_kos WHERE nama = %s",(nama,))
  conn.commit()
  cur.close()
  conn.close()

# tambahPenghuni("iqbal", 20)
hapusPenghuni("iqbal")
# lihatPenghuni()
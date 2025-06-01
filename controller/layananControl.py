import controller.database as db

def read():
  conn,cur = db.connectDB()
  try:
    query = "SELECT * FROM layanan"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except:
    input("Terjadi kesalahan pada controller read layanan")
    return None
  finally:
    conn.close()

def add(nama, harga):
  conn, cur = db.connectDB()
  try:
    query = "INSERT INTO layanan(nama_layanan, harga) VALUES(%s,%s)"
    cur.execute(query, (nama,harga))
    conn.commit()
    return True
  except:
    input("Terjadi kesalahan pada controller add layanan")
    return False
  finally:
    conn.close()

def update(nama, harga, id):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE layanan SET nama_layanan=%s, harga=%s WHERE id_layanan=%s"
    cur.execute(query, (nama,harga,id))
    conn.commit()
    return True
  except:
    input("Terjadi kesalahan pada controller update layanan")
    return False
  finally:
    conn.close()

def delete(id):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE layanan SET status = false WHERE id_layanan=%s"
    cur.execute(query, (id,))
    conn.commit()
    return True
  except:
    input("Terjadi kesalahan pada controller update layanan")
    return False
  finally:
    conn.close()


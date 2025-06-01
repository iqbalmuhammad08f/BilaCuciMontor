import controller.database as db

def add(nama,harga,durasi):
  conn, cur = db.connectDB()
  try:
    query = "INSERT INTO paket_member(nama, harga, durasi) VALUES(%s,%s,%s)"
    cur.execute(query, (nama,harga,durasi))
    conn.commit()
    return True
  except:
    input("Terjadi kesalahan pada controller add paket member")
    return False
  finally:
    conn.close()

def read():
  conn, cur = db.connectDB()
  try:
    query = "SELECT * FROM paket_member"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except:
    input("Terjadi kesalahan pada controller read paket member")
    return None
  finally:
    conn.close()

def update(harga, durasi, id):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE paket_member SET harga=%s, durasi=%s WHERE id_paket=%s"
    cur.execute(query, (harga, durasi, id))
    conn.commit()
    return True
  except:
    input("Terjadi kesalahan pada controller update paket member")
    return False
  finally:
    conn.close()

def delete(id):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE paket_member SET status = false WHERE id_paket=%s"
    cur.execute(query, (id,))
    conn.commit()
    return True
  except:
    input("Terjadi kesalahan pada controller delete paket member")
    return False
  finally:
    conn.close()
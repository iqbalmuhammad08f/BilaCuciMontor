import controller.database as db

def add(nama, email, nomor_telepon, alamat, role):
  conn, cur = db.connectDB()
  try:
    query = "INSERT INTO karyawan(nama, email, nomor_hp, alamat, role) VALUES(%s, %s, %s, %s, %s)"
    cur.execute(query, (nama, email, nomor_telepon, alamat, role))
    conn.commit()
    return True
  except Exception:
    input("terjadi kesalahan pada controller karyawan")
    return False
  finally:
    conn.close()

def update(nama, email, nomor_telepon, alamat, role):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE karyawan SET email=%s, nomor_hp=%s, alamat=%s, role=%s WHERE nama=%s"
    cur.execute(query, (email, nomor_telepon, alamat, role, nama))
    conn.commit()
    return True
  except Exception:
    input("terjadi kesalahan pada controller karyawan")
    return False
  finally:
    conn.close()

def delete(nama):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE karyawan SET status=false WHERE nama=%s"
    cur.execute(query, (nama,))
    conn.commit()
    return True
  except Exception:
    input("terjadi kesalahan pada controller karyawan")
    return False
  finally:
    conn.close()

def read():
  conn, cur = db.connectDB()
  try:
    query = "SELECT * FROM karyawan"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except Exception:
    input("terjadi kesalahan pada controller karyawan")
    return None
  finally:
    conn.close()

def getIdKaryawan(nama):
  conn, cur = db.connectDB()
  try:
    query = "SELECT id_karyawan FROM karyawan WHERE nama=%s"
    cur.execute(query, (nama,))
    data = cur.fetchone()
    return data[0] if data else None
  except Exception:
    input("terjadi kesalahan pada controller getIdKaryawan")
    return None
  finally:
    conn.close()
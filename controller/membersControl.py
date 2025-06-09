import controller.database as db
# import database as db

def read():
  conn, cur = db.connectDB()
  try:
    query = "SELECT * FROM members"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except Exception:
    input("Terjadi kesalahan pada controller read members")
    return None
  finally:
    conn.close()

def readmember(username):
  conn, cur = db.connectDB()
  try:
    query = "SELECT m.id_member, u.username, m.nama FROM members m JOIN users u ON m.id_user = u.id_user WHERE u.role = 'member' AND u.username = %s AND m.status = true"
    cur.execute(query, (username,))
    data = cur.fetchall()
    return data
  except Exception:
    input("Terjadi kesalahan pada controller read members")
    return None
  finally:
    conn.close()

print(readmember("jamal01"))

def add(id_user,nama):
  conn, cur = db.connectDB()
  try:
    query = "INSERT INTO members(nama,id_user) VALUES(%s, %s)"
    cur.execute(query,(nama,id_user))
    conn.commit()
  except Exception:
    input("Terjadi kesalahan pada controller add members,", Exception)
    return None
  finally:
    conn.close()

def readOne(id_member):
  conn, cur = db.connectDB()
  try:
    query = "SELECT * FROM members WHERE id_user = %s"
    cur.execute(query, (id_member,))
    data = cur.fetchone()
    return data
  except Exception:
    input("Terjadi kesalahan pada controller readOne members,", Exception)
    return None
  finally:
    conn.close()

def updateTanggalBerakhir(id_member, tanggal_berakhir):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE members SET tanggal_berakhir = %s, status = true WHERE id_member = %s"
    cur.execute(query, (tanggal_berakhir, id_member))
    conn.commit()
  except Exception:
    input("Terjadi kesalahan pada controller updateTanggalBerakhir members,", Exception)
    return None
  finally:
    conn.close()

def updateStatus():
  conn, cur = db.connectDB()
  try:
    query = "UPDATE members SET status = false WHERE tanggal_berakhir < NOW()"
    cur.execute(query)
    conn.commit()
  except Exception:
    input("Terjadi kesalahan pada controller updateStatus members,", Exception)
    return None
  finally:
    conn.close()
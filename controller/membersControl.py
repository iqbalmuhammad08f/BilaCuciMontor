import controller.database as db

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
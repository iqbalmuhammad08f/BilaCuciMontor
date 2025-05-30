import controller.database as db

def readAdmin():
  conn, cur = db.connectDB()
  try:
    query = "SELECT username,password FROM users WHERE role = 'admin'"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except Exception:
    input("terjadi kesalahan pada controller users")
    return None
  finally:
    conn.close()

def readKasir():
  conn, cur = db.connectDB()
  try:
    query = "SELECT username,password FROM users WHERE role = 'kasir'"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except Exception:
    input("terjadi kesalahan pada controller users")
    return None
  finally:
    conn.close()

def add(username, password):
  conn, cur = db.connectDB()
  try:
    query = "INSERT INTO users(username, password, role) VALUES(%s, %s, 'member') RETURNING id_user"
    cur.execute(query, (username, password))
    id_user = cur.fetchone()[0]
    conn.commit()
    return id_user
  except Exception:
    input("terjadi kesalahan pada controller users")
    return None
  finally:
    conn.close()




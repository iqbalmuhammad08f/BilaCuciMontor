import controller.database as db
# import database as db

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
    query = "SELECT * FROM users WHERE role = 'kasir'"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except Exception:
    input("terjadi kesalahan pada controller users")
    return None
  finally:
    conn.close()

def readMember():
  conn, cur = db.connectDB()
  try:
    query = "SELECT * FROM users WHERE role = 'member'"
    cur.execute(query)
    data = cur.fetchall()
    return data
  except Exception:
    input("terjadi kesalahan pada controller users")
    return None
  finally:
    conn.close()

def editKasir(id_kasir, username, password):
  conn, cur = db.connectDB()
  try:
    query = "UPDATE users SET username = %s, password = %s WHERE id_user = %s"
    cur.execute(query, (username, password, id_kasir))
    conn.commit()
    return True
  except Exception:
    input("terjadi kesalahan pada controller users")
    return False
  finally:
    conn.close()
  
def addKasir(username, password):
  conn, cur = db.connectDB()
  try:
    query = "INSERT INTO users(username, password, role) VALUES(%s, %s, 'kasir')"
    cur.execute(query, (username, password))
    conn.commit()
    return True
  except Exception:
    input("terjadi kesalahan pada controller users")
    return False
  finally:
    conn.close()

def addMember(username, password):
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




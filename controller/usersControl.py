import controller.database as db

def read():
  conn, cur = db.connetDB()
  query = "SELECT * FROM users"
  cur.execute(query)
  data = cur.fetchall()
  conn.close()
  return data

print([user[1] for user in read()])

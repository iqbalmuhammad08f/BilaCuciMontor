import database as db

def read():
  conn, cur = db.connetDB()
  query = "SELECT * FROM members"
  cur.execute(query)
  data = cur.fetchall()
  conn.close()
  return data

user = [user[1] for user in read()]
print(user)
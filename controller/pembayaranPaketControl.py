import controller.database as db

def add(id_member, id_paket,total):
    conn, cur = db.connectDB()
    try:
        query = "INSERT INTO pembayaran_member(id_member, id_paket, total) VALUES(%s, %s, %s)"
        cur.execute(query, (id_member, id_paket, total))
        conn.commit()
        return True
    except Exception as e:
        input(f"Terjadi kesalahan pada controller add pembayaran paket: {e}")
        return False
    finally:
        conn.close()

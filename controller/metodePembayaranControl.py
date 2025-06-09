import controller.database as db

def read():
    conn, cur = db.connectDB()
    try:
        query = "SELECT * FROM metode_pembayaran"
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception:
        input("Terjadi kesalahan pada controller read metode pembayaran")
        return None
    finally:
        conn.close()
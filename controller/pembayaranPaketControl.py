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

def readOne(id_member):
    conn, cur = db.connectDB()
    try:
        query = "SELECT pm2.nama, TO_CHAR(pm.tanggal, 'YYYY-MM-DD HH24:MI:SS') AS tanggal, pm.total FROM pembayaran_member pm JOIN paket_member pm2 ON pm.id_paket = pm2.id_paket WHERE id_member = %s"
        cur.execute(query, (id_member,))
        data = cur.fetchall()
        return data
    except Exception as e:
        input(f"Terjadi kesalahan pada controller readOne pembayaran paket: {e}")
        return None
    finally:
        conn.close()

def getAllTotalPembayaran():
    conn, cur = db.connectDB()
    try:
        query = "SELECT SUM(pm.total) FROM pembayaran_member pm"
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception as e:
        input(f"Terjadi kesalahan pada controller getAll: {e}")
        return None
    finally:
        conn.close()

def getAllPembayaran():
    conn, cur = db.connectDB()
    try:
        query = "SELECT DATE(tanggal), sum(total) FROM pembayaran_member GROUP BY DATE(tanggal), total ORDER BY DATE(tanggal) DESC"
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception as e:
        input(f"Terjadi kesalahan pada controller getalltransaksi: {e}")
        return None
    finally:
        conn.close()
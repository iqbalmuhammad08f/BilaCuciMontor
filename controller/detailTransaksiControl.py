import controller.database as db

def add(id_transaksi, id_layanan, plat, nama_kendaraan, subtotal=0):
    conn, cur = db.connectDB()
    try:
        query = "INSERT INTO detail_transaksi(id_transaksi, id_layanan, plat, nama_kendaraan, subtotal) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(query, (id_transaksi, id_layanan, plat, nama_kendaraan, subtotal))
        conn.commit()
    except Exception as e:
        input(f"Terjadi kesalahan pada controller add detail transaksi: {e}")
        return None
    finally:
        conn.close()
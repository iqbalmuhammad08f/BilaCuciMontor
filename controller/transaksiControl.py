import controller.database as db

def addTransaksiMember(id_member, id_karyawan):
    conn, cur = db.connectDB()
    try:
        query = "INSERT INTO transaksi(id_member, id_karyawan) VALUES(%s, %s) RETURNING id_transaksi"
        cur.execute(query, (id_member, id_karyawan))
        id_transaksi = cur.fetchone()[0]
        conn.commit()
        return id_transaksi
    except Exception as e:
        input(f"Terjadi kesalahan pada controller add transaksi member: {e}")
        return None
    finally:
        conn.close()

def addTransaksiNonMember(id_karyawan, id_metode,uang):
    conn, cur = db.connectDB()
    try:
        query = "INSERT INTO transaksi(id_karyawan, id_metode, uang) VALUES(%s, %s, %s) RETURNING id_transaksi"
        cur.execute(query, (id_karyawan, id_metode, uang))
        id_transaksi = cur.fetchone()[0]
        conn.commit()
        return id_transaksi
    except Exception as e:
        input(f"Terjadi kesalahan pada controller add transaksi non-member: {e}")
        return None
    finally:
        conn.close()

def updatetotalTransaksi(id_transaksi, total):
    conn, cur = db.connectDB()
    try:
        query = "UPDATE transaksi SET total = %s WHERE id_transaksi = %s"
        cur.execute(query, (total, id_transaksi))
        conn.commit()
    except Exception as e:
        input(f"Terjadi kesalahan pada controller update total transaksi: {e}")
        return None
    finally:
        conn.close()
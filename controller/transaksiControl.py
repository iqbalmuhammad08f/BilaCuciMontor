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

def getAllTotalTransaksi():
    conn, cur = db.connectDB()
    try:
        query = "SELECT SUM(transaksi.total) FROM transaksi"
        cur.execute(query)
        total = cur.fetchall()
        return total
    except Exception as e:
        input(f"Terjadi kesalahan pada controller get total transaksi: {e}")
        return None
    finally:
        conn.close()

def getAllTransaksi():
    conn, cur = db.connectDB()
    try:
        query = "SELECT tanggal, SUM(total) FROM transaksi WHERE total > 0 GROUP BY tanggal, total ORDER BY tanggal DESC"
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception as e:
        input(f"Terjadi kesalahan pada controller getalltransaksi: {e}")
        return None
    finally:
        conn.close()

def getAllDetailTransaksi():
    conn, cur = db.connectDB()
    try:
        query = "SELECT to_char(dt.tanggal, 'yyyy-mm-dd, hh:mi:ss'), k.nama, m.nama, dt.subtotal, mp.nama_metode,dt.nama_kendaraan, dt.plat FROM transaksi t FUll JOIN detail_transaksi dt on t.id_transaksi = dt.id_transaksi FUll JOIN karyawan k ON t.id_karyawan = k.id_karyawan FULL JOIN metode_pembayaran mp ON mp.id_metode = t.id_metode LEFT JOIN members m ON t.id_member = m.id_member ORDER BY dt.tanggal DESC"
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception as e:
        input(f"Terjadi kesalahan pada controller getalltransaksi: {e}")
        return None
    finally:
        conn.close()
import controller.layananControl as lc
import controller.karyawanControl as kc
import controller.membersControl as mc
import controller.metodePembayaranControl as mpc
import controller.transaksiControl as tc
import controller.detailTransaksiControl as dtc
import os
import pandas as pd
import tabulate as tb

def kasirMenu(nama_kasir):
  while True:
    id_karyawan = kc.getIdKaryawan(nama_kasir)
    os.system("cls")
    print("=== Menu Kasir ===")
    print(f"Selamat datang, {nama_kasir}")
    print("1. Transaksi")
    print("2. Lihat Laporan")
    print("0. Logout")
    user = input("Masukkan pilihan :")
    if user == "1":
      transaksi(id_karyawan)
    elif user == "2":
      print()
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")

def transaksi(id_karyawan):
  def transaksiMember(id_karyawan, layanan):
    while True:
      username = input("Masukkan username: ")
      data_member = mc.readmember(username)
      if data_member:
        id_member = data_member[0][0]
        kendaraan = input("Masukkan nama kendaraan: ")
        plat = input("Masukkan plat kendaraan: ")
        id_transaksi = tc.addTransaksiMember(id_member, id_karyawan)
        dtc.add(id_transaksi, layanan, plat, kendaraan)
        input("Transaksi berhasil, tekan Enter untuk melanjutkan")
        break
      else:
        input("Username tidak ditemukan, tekan Enter untuk mengulangi")
        continue
  
  def transaksiNonMember(id_karyawan, layanan, df_metode, harga_layanan):
    run = True
    list_kendaraan = []
    while run:
      kendaraan = input("Masukkan nama kendaraan: ")
      plat = input("Masukkan plat kendaraan: ")
      konfirmasi = input("Apakah ingin menambahkan kendaraan lagi? (y/t): ").lower()
      if konfirmasi == "y":
        list_kendaraan.append({"kendaraan": kendaraan, "plat": plat})
        continue
      elif konfirmasi == "t":
        list_kendaraan.append({"kendaraan": kendaraan, "plat": plat})
        while run:
          os.system("cls")
          total = 0
          for i in list_kendaraan:
            total += harga_layanan
          print("=== Metode Pembayaran ===")
          print(tb.tabulate(df_metode, headers="keys", tablefmt="psql", showindex=False))
          print(f"Total: {total}")
          metode_pembayaran = int(input("Masukkan Id metode pembayaran :"))
          if metode_pembayaran in df_metode["ID"].values:
            if metode_pembayaran == 1:
              try:
                uang = int(input("Masukkan jumlah uang: "))
                if uang < total:
                  input("Jumlah uang tidak cukup, tekan Enter untuk mengulangi")
                  continue
                else:
                  id_transaksi = tc.addTransaksiNonMember(id_karyawan, metode_pembayaran, uang)
                  for kendaraan in list_kendaraan:
                    dtc.add(id_transaksi, layanan, kendaraan["plat"], kendaraan["kendaraan"],harga_layanan)
                  tc.updatetotalTransaksi(id_transaksi, total)
                  kembalikan = uang - total
                  if kembalikan > 0:
                    os.system("cls")
                    print(f"kembalian: {kembalikan}")
                    input("Transaksi berhasil, Enter untuk kembali")
                    run = False
                    break
                  else:
                    input("Transaksi berhasil, Enter untuk kembali")
                    run = False
                    break
              except ValueError:
                input("Input tidak valid, tekan Enter untuk mengulangi")
                continue
            elif metode_pembayaran == 2:
              id_transaksi = tc.addTransaksiNonMember(id_karyawan, metode_pembayaran, total)
              for kendaraan in list_kendaraan:
                dtc.add(id_transaksi, layanan, kendaraan["plat"], kendaraan["kendaraan"],harga_layanan)
              tc.updatetotalTransaksi(id_transaksi, total)
              input("Transaksi berhasil, Enter untuk kembali")
              run = False
              break
          else:
            input("Metode pembayaran tidak valid, tekan Enter untuk mengulangi")
            continue
      else:
        input("Input tidak valid, tekan Enter untuk mengulangi")
        continue

  while True:
    try:
      data_layanan = [p for p in lc.read() if p[3] == True]
      df_layanan = pd.DataFrame(data_layanan, columns=["ID", "Nama", "Harga", "Tersedia"])
      df_layanan.drop(columns=["Tersedia"], inplace=True)
      metode_pembayaran = mpc.read()
      df_metode = pd.DataFrame(metode_pembayaran, columns=["ID", "Nama Metode","status"])
      df_metode.drop(columns=["status"], inplace=True,)
      
      os.system("cls")
      print("=== Transaksi ===")
      print(tb.tabulate(df_layanan, headers="keys", tablefmt="psql", showindex=False))
      pilih_layanan = int(input("Masukkan ID layanan yang ingin dipilih [0 untuk kembali]: "))
      if pilih_layanan in df_layanan["ID"].values:
        while True:
          harga_layanan = df_layanan[df_layanan["ID"] == pilih_layanan]["Harga"].values[0]
          is_member = input("Apakah member? (y/t): ").lower()
          if is_member == "y":
            transaksiMember(id_karyawan, pilih_layanan)
            break
          elif is_member == "t":
            transaksiNonMember(id_karyawan, pilih_layanan,df_metode, int(harga_layanan))
            break
          else:
            input("Input tidak valid, tekan Enter untuk mengulangi")
            continue
      elif pilih_layanan == 0:
        break
      else:
        input("pilihan layanan tidak valid, tekan Enter untuk mengulangi")
        continue
    except ValueError:
      input("Input tidak valid, tekan Enter untuk mengulangi")
      continue
    
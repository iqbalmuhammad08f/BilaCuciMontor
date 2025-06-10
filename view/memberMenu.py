import controller.usersControl as uc
import controller.membersControl as mc
import controller.paketMemberControl as pmc
import controller.pembayaranPaketControl as ppc

import os
import pandas as pd
import tabulate as tb

def memberMenu(nama_member):
  while True:
    mc.updateStatus()
    id_user = uc.getmemberId(nama_member)
    member = mc.readOne(id_user)
    status = member[7]
    tanggal_berakhir = member[6]
    tanggal_sekarang = pd.Timestamp.now().normalize()
    os.system("cls")
    print("=== Menu Member ===")
    print(f"Selamat datang, {member[1]}")
    print(f"Status: {'Aktif' if status else 'Tidak Aktif'}")
    print("1. Pembayaran langanan")
    print("2. Histori")
    print("3. Ubah data diri")
    print("4. Informasi akun")
    print("0. Logout")
    user = input("Masukkan pilihan :")
    if user == "1":
      pembayaranLangganan(member[0], status, tanggal_berakhir, tanggal_sekarang)
    elif user == "2":
      while True:
        os.system("cls")
        print("=== Histori ===")
        print("1. Histori mencuci")
        print("2. Histori pembayaran langganan")
        print("0. Kembali")
        user = input("Masukkan pilihan :")
        if user == "1":
          historiMencuci(member[0])
        elif user == "2":
          historiPembayaranLangganan(member[0])
        elif user == "0":
          break
        else:
          input("Pilihan tidak valid, tekan Enter untuk mengulangi")
    elif user == "3":
      print()
    elif user == "4":
      print()
    elif user == "0":
      break
    else:
      input("Pilihan tidak valid, tekan Enter untuk melanjutkan")

def pembayaranLangganan(id_member, status, tanggal_berakhir, tanggal_sekarang):
  run = True
  while run:
    os.system("cls")
    print("=== Pembayaran Langganan ===")
    paket = [p for p in pmc.read() if p[4] == True]
    df = pd.DataFrame(paket, columns=["ID Paket", "Nama Paket", "Harga", "Durasi/hari", "Status"])
    df.drop(columns=["Status"], inplace=True)
    print(tb.tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    while run:
      try:
        id_paket = int(input("Masukkan ID Paket yang ingin dibeli [0 untuk kembali]: "))
        if id_paket == 0:
          run = False
          break
        elif id_paket in df["ID Paket"].values:
          while run:
            try:
              uang = int(input("Masukkan jumlah uang yang akan dibayarkan: "))
              harga,durasi = df.loc[df["ID Paket"] == id_paket, ["Harga", "Durasi/hari"]].values[0]
              if uang == harga:
                ppc.add(id_member, id_paket, uang)
                if status == True:
                  mc.updateTanggalBerakhir(id_member, tanggal_berakhir + pd.Timedelta(days=durasi))
                else:
                  mc.updateTanggalBerakhir(id_member, tanggal_sekarang + pd.Timedelta(days=durasi))
                input("Pembayaran berhasil, tekan Enter untuk melanjutkan")
                run = False
              else:
                input("Jumlah uang tidak sesuai, tekan Enter untuk mengulangi")
            except ValueError:
              input("Input tidak valid, tekan Enter untuk mengulangi")
        else:
          input("ID Paket tidak valid, tekan Enter untuk mengulangi")
      except ValueError:
        input("Input tidak valid, tekan Enter untuk mengulangi")

def historiMencuci(id_member):
    # Implementasi histori mencuci
    
    pass

def historiPembayaranLangganan(id_member):
  list_pembayaran = ppc.readOne(id_member)
  if list_pembayaran:
    df = pd.DataFrame(list_pembayaran, columns=["Nama", "Tanggal", "Total"])
    df.index += 1
    print("=== Histori Pembayaran Langganan ===")
    print(tb.tabulate(df, headers='keys', tablefmt='psql'))
    input("Tekan Enter untuk kembali")
  else:
    input("Tidak ada histori pembayaran langganan, tekan Enter untuk kembali")

def ubahDataDiri(id_member):
    # Implementasi ubah data diri
    pass
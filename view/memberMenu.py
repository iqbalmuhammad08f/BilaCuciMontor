import controller.usersControl as uc
import controller.membersControl as mc
import controller.paketMemberControl as pmc
import controller.pembayaranPaketControl as ppc

import os
import pandas as pd
import tabulate as tb

def memberMenu(nama_member):
  id_user = uc.getmemberId(nama_member)
  while True:
    member = mc.readOne(id_user)
    os.system("cls")
    print("=== Menu Member ===")
    print(f"Selamat datang, {member[1]}")
    print("1. Pembayaran langanan")
    print("2. Histori")
    print("3. Ubah data diri")
    print("4. Informasi akun")
    print("0. Logout")
    user = input("Masukkan pilihan :")
    if user == "1":
      pembayaranLangganan(member[0])
    elif user == "2":
      print()
    elif user == "3":
      print()
    elif user == "4":
      print()
    elif user == "0":
      break
    else:
      input("Pilihan tidak valid, tekan Enter untuk melanjutkan")

def pembayaranLangganan(id_member):
  run = True
  while run:
    os.system("cls")
    print("=== Pembayaran Langganan ===")
    paket = [p for p in pmc.read() if p[4] == True]
    df = pd.DataFrame(paket, columns=["ID Paket", "Nama Paket", "Harga", "Durasi", "Status"])
    df.drop(columns=["Status","Durasi"], inplace=True)
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
              if uang == df.loc[df["ID Paket"] == id_paket, "Harga"].values[0]:
                result = ppc.add(id_member, id_paket, uang)
                if result:
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

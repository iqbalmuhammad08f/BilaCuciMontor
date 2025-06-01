import controller.usersControl as uc
import controller.karyawanControl as kc
import controller.layananControl as lc
import controller.paketMemberControl as pmc

import os
import pandas as pd
import tabulate as tb

def adminMenu():
  while True:
    os.system("cls")
    print("=== Dasboard Admin ===")
    print("1. Melihat laporan keuangan")
    print("2. Mengelola akun kasir")
    print("3. Mengelola karyawan")
    print("4. Mengelola harga layanan")
    print("5. Mengelola harga member")
    print("6. melihat member")
    print("7. Melihat history transaksi")
    print("0. logout")
    user = input("Masukkan pilihan :")
    if user == "1":
      print()
    elif user == "2":
      mengelolaAkunKasir()
    elif user == "3":
      mengelolaKaryawan()
    elif user == "4":
      mengelolaHargaLayanan()
    elif user == "5":
      mengelolaHargaMember()
    elif user == "6":
      print()
    elif user == "7":
      print()
    elif user == "0":
      print()
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")

def mengelolaAkunKasir():
  def tambahAkunKasir():
    run = True
    while run:
      os.system("cls")
      print("=== Tambah Akun Kasir ===")
      username = input("Masukkan username [0 untuk kembali]: ")
      if username == "0":
        break
      while run:
        password = input("Masukkan password: ")
        repreatPw = input("Ulangi password: ")
        if password == repreatPw:
          uc.addKasir(username,password)
          input("Akun kasir berhasil ditambahkan, Enter untuk kembali")
          run = False
        else:
          input("Password tidak sama, Enter untuk mencoba lagi")
          continue

  def editAkunKasir():
    run = True
    while run:
      os.system("cls")
      print("=== Edit Akun Kasir ===")
      username = input("Masukkan username baru [0 untuk kembali]: ")
      if username == "0":
        break
      while run:
        password = input("Masukkan password baru: ")
        repreatPw = input("Ulangi password: ")
        if password == repreatPw:
          id_kasir = uc.readKasir()[0][0]
          uc.editKasir(id_kasir, username, password)
          input("Akun kasir berhasil diedit, Enter untuk kembali")
          run = False
        else:
          input("Password tidak sama, Enter untuk mencoba lagi")
          continue

  def lihatAkunKasir():
    os.system("cls")
    print("=== Lihat Akun Kasir ===")
    kasir = uc.readKasir()
    print(f"Username : {kasir[0][1]}")
    print(f"Password : {kasir[0][2]}")
    input("Tekan Enter untuk kembali")

  while True:
    os.system("cls")
    print("=== Mengelola Akun Kasir ===")
    print("1. Tambah akun")
    print("2. Edit akun")
    print("3. lihat akun")
    print("0. Kembali")
    user = input("Masukkan pilihan :")
    if user == "1":
      if uc.readKasir() != []:
        input("Tidak dapat membuat akun kasir, Enter untuk kembali")
        continue
      else:
        tambahAkunKasir()
    elif user == "2":
      if uc.readKasir() == []:
        input("Belum meiliki akun kasir, Enter untuk kembali")
        continue
      else:
        editAkunKasir()
    elif user == "3":
      if uc.readKasir() == []:
        input("Belum memiliki akun kasir, Enter untuk kembali")
        continue
      else:
        lihatAkunKasir()
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")

def mengelolaKaryawan():
  def tambahKaryawan():
    while True:
      os.system("cls")
      print("=== Tambah Karyawan ===")
      list_role = ["kasir", "pekerja"]
      for role in list_role:
        print(f"- {role}")
      role = input("Masukkan role karyawan [0 untuk kembali]: ").lower()
      if role == "0":
        break
      if role not in list_role:
        input("Role tidak sesuai, Enter untuk mengulangi")
        continue
      else:
        nama = input("Masukkan nama karyawan: ").lower()
        email = input("Masukkan email karyawan: ")
        nomor_telepon = input("Masukkan nomor telepon karyawan: ")
        alamat = input("Masukkan alamat karyawan: ")
        kc.add(nama, email, nomor_telepon, alamat, role)
        input("Karyawan berhasil ditambahkan, Enter untuk kembali")
        break

  def editKaryawan():
    run = True
    while run:
      os.system("cls")
      print("=== Edit Karyawan ===")
      nama = input("Masukkan nama karyawan yang ingin diedit [0 untuk kembali]: ").lower()
      if nama == "0":
        break
      karyawan = kc.read()
      for k in karyawan:
        if k[0] == nama:
          email = input("Masukkan email baru: ")
          nomor_telepon = input("Masukkan nomor telepon baru: ")
          alamat = input("Masukkan alamat baru: ")
          while True:
            role = input("Masukkan role baru(kasir/pekerja): ").lower()
            if role in ["kasir", "pekerja"]:
              break
            else:
              input("Role tidak sesuai, Enter untuk mencoba lagi")
          kc.update(nama, email, nomor_telepon, alamat, role)
          input("Karyawan berhasil diedit, Enter untuk kembali")
          run = False
          break
      else:
        input("Karyawan tidak ditemukan, Enter untuk mencoba lagi")
        continue

  def lihatKaryawan():
    os.system("cls")
    print("=== Lihat Karyawan ===")
    karyawan = []
    for k in kc.read():
        if k[7] == True:  
            karyawan.append(k)
    df = pd.DataFrame(karyawan, columns=["ID", "Nama", "Email", "Nomor Telepon", "Alamat", "Role", "Tanggal Masuk", "Status"])
    df.drop(columns=["ID", "Status"], inplace=True)
    df.index += 1
    print(tb.tabulate(df, headers="keys", tablefmt="psql"))
    input("Tekan Enter untuk kembali")


  def hapusKaryawan():
    run = True
    while run:
      os.system("cls")
      print("=== Hapus Karyawan ===")
      nama = input("Masukkan nama karyawan yang ingin dihapus [0 untuk kembali]: ").lower()
      if nama == "0":
        break
      karyawan = kc.read()
      for k in karyawan:
        if k[1] == nama:
          kc.delete(nama)
          input("Karyawan berhasil dihapus, Enter untuk kembali")
          run = False
          break
      else:
        input("Karyawan tidak ditemukan, Enter untuk mencoba lagi")
        continue

  while True:
    os.system("cls")
    print("=== Mengelola Karyawan ===")
    print("1. Tambah karyawan")
    print("2. Edit karyawan")
    print("3. Lihat karyawan")
    print("4. Hapus karyawan")
    print("0. Kembali")
    user = input("Masukkan pilihan :")
    if user == "1":
      tambahKaryawan()
    elif user == "2":
      if kc.read() == []:
        input("Belum memiliki karyawan, Enter untuk kembali")
        continue
      else:
        editKaryawan()
    elif user == "3":
      if kc.read() == []:
        input("Belum memiliki karyawan, Enter untuk kembali")
        continue
      else:
        lihatKaryawan()
    elif user == "4":
      if kc.read() == []:
        input("Belum memiliki karyawan, Enter untuk kembali")
        continue
      else:
        hapusKaryawan()
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")

def mengelolaHargaLayanan():
  def tambahLayanan():
    run = True
    while run:
      os.system("cls")
      nama = input("Masukkan nama layanan [0 untuk kembali]:")
      if nama == "0":
        break
      layanan = lc.read()
      for l in layanan:
        if l[1] == nama:
          input("Layanan sudah ada, Enter untuk mencoba lagi")
          continue
      else:
        while run:
          try:
            harga = int(input("Masukkan harga layanan :"))
            if harga > 0:
              lc.add(nama, harga)
              input("Layanan berhasil ditambahkan, Enter untuk kembali")
              run = False
              break
            else:
              input("Harga harus lebih dari 0, Enter untuk mencoba lagi")
          except ValueError:
            input("Harga tidak valid, Enter untuk mencoba lagi")

  def editLayanan():
    run = True
    while run:
      os.system("cls")
      print("=== Edit Layanan ===")
      nama = input("Masukkan nama layanan yang ingin diedit [0 untuk kembali]: ")
      if nama == "0":
        break
      layanan = lc.read()
      for l in layanan:
        if l[1] == nama:
          while run:
            try:
              harga = int(input("Masukkan harga baru: "))
              if harga > 0:
                lc.update(nama, harga, l[0])
                input("Layanan berhasil diedit, Enter untuk kembali")
                run = False
                break
              else:
                input("Harga harus lebih dari 0, Enter untuk mencoba lagi")
            except ValueError:
              input("Harga tidak valid, Enter untuk mencoba lagi")
          break
      else:
        input("Layanan tidak ditemukan, Enter untuk mencoba lagi")
        continue

  def lihatLayanan():
    os.system("cls")
    print("=== Lihat Layanan ===")
    layanan = []
    for l in lc.read():
      if l[3] == True:  
        layanan.append(l) 
    df = pd.DataFrame(layanan, columns=["ID", "Nama", "Harga", "Status"])
    df.drop(columns=["ID", "Status"], inplace=True)
    df.index += 1
    print(tb.tabulate(df, headers="keys", tablefmt="psql"))
    input("Tekan Enter untuk kembali")

  def hapusLayanan():
    run = True
    while run:
      os.system("cls")
      print("=== Hapus Layanan ===")
      nama = input("Masukkan nama layanan yang ingin dihapus [0 untuk kembali]: ")
      if nama == "0":
        break
      layanan = lc.read()
      for l in layanan:
        if l[1] == nama:
          lc.delete(l[0])
          input("Layanan berhasil dihapus, Enter untuk kembali")
          run = False
          break
      else:
        input("Layanan tidak ditemukan, Enter untuk mencoba lagi")
        continue

  while True:
    os.system("cls")
    print("=== Mengelola Harga Layanan ===")
    print("1. Tambah layanan")
    print("2. Edit layanan")
    print("3. Lihat Layanan")
    print("4. Hapus Layanan")
    print("0. Exit")
    user = input("Masukkan Pilihan :")
    if user == "1":
      tambahLayanan()
    elif user == "2":
      if lc.read() == []:
        input("Belum memiliki layanan, Enter untuk kembali")
        continue
      else:
        editLayanan()
    elif user == "3":
      if lc.read() == []:
        input("Belum memiliki layanan, Enter untuk kembali")
        continue
      else:
        lihatLayanan()
    elif user == "4":
      if lc.read() == []:
        input("Belum memiliki layanan, Enter untuk kembali")
        continue
      else:
        hapusLayanan()
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")

def mengelolaHargaMember():
  def tambahHargaMember():
    run = True
    while run:
      os.system("cls")
      print("=== Tambah Harga Member ===")
      nama = input("Masukkan nama paket member [0 untuk kembali]: ")
      if nama == "0":
        break
      paket = pmc.read()
      for p in paket:
        if p[1] == nama:
          input("Paket member sudah ada, Enter untuk mencoba lagi")
          continue
      else:
        while True:
          try:
            harga = int(input("Masukkan harga paket member :"))
            durasi = int(input("Masukkan durasi paket member (dalam hari): "))
            if harga > 0 and durasi > 0:
              pmc.add(nama, harga, durasi)
              input("Paket member berhasil ditambahkan, Enter untuk kembali")
              run = False
              break
            else:
              input("Harga dan durasi harus lebih dari 0, Enter untuk mencoba lagi")
          except ValueError:
            input("Harga atau durasi tidak valid, Enter untuk mencoba lagi")
  
  def editHargaMember():
    run = True
    while run:
      os.system("cls")
      print("=== Edit Harga Member ===")
      nama = input("Masukkan nama paket member yang ingin diedit [0 untuk kembali]: ")
      if nama == "0":
        break
      paket = pmc.read()
      for p in paket:
        if p[1] == nama:
          while run:
            try:
              harga = int(input("Masukkan harga baru: "))
              durasi = int(input("Masukkan durasi baru (dalam hari): "))
              if harga > 0 and durasi > 0:
                pmc.update(harga, durasi, p[0])
                input("Paket member berhasil diedit, Enter untuk kembali")
                run = False
                break
              else:
                input("Harga dan durasi harus lebih dari 0, Enter untuk mencoba lagi")
            except ValueError:
              input("Harga atau durasi tidak valid, Enter untuk mencoba lagi")
          break
      else:
        input("Paket member tidak ditemukan, Enter untuk mencoba lagi")
        continue

  def lihatHargaMember():
    os.system("cls")
    print("=== Lihat Harga Member ===")
    paket = []
    for p in pmc.read():
      if p[4] == True:  
        paket.append(p) 
    df = pd.DataFrame(paket, columns=["ID", "Nama", "Harga", "Durasi", "Status"])
    df.drop(columns=["ID", "Status"], inplace=True)
    df.index += 1
    print(tb.tabulate(df, headers="keys", tablefmt="psql"))
    input("Tekan Enter untuk kembali")

  def hapusHargaMember():
    run = True
    while run:
      os.system("cls")
      print("=== Hapus Harga Member ===")
      nama = input("Masukkan nama paket member yang ingin dihapus [0 untuk kembali]: ")
      if nama == "0":
        break
      paket = pmc.read()
      for p in paket:
        if p[1] == nama:
          pmc.delete(p[0])
          input("Paket member berhasil dihapus, Enter untuk kembali")
          run = False
          break
      else:
        input("Paket member tidak ditemukan, Enter untuk mencoba lagi")
        continue
      
  while True:
    os.system("cls")
    print("=== Mengelola Harga Member ===")
    print("1. Tambah harga member")
    print("2. Edit harga member")
    print("3. Lihat harga member")
    print("4. Hapus harga member")
    print("0. Kembali")
    user = input("Masukkan pilihan :")
    if user == "1":
      tambahHargaMember()
    elif user == "2":
      if pmc.read() == []:
        input("Belum memiliki harga member, Enter untuk kembali")
        continue
      else:
        editHargaMember()
    elif user == "3":
      if pmc.read() == []:
        input("Belum memiliki harga member, Enter untuk kembali")
        continue
      else:
        lihatHargaMember()
    elif user == "4":
      if pmc.read() == []:
        input("Belum memiliki harga member, Enter untuk kembali")
        continue
      else:
        hapusHargaMember()
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")
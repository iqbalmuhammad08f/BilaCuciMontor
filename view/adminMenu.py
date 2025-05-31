import os
import controller.usersControl as uc
import controller.karyawanControl as kc
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
    print("0. Exit")
    user = input("Masukkan pilihan :")
    if user == "1":
      print()
    elif user == "2":
      mengelolaAkunKasir()
    elif user == "3":
      mengelolaKaryawan()
    elif user == "4":
      print()
    elif user == "5":
      print()
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
      username = input("Masukkan username: ")
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
      username = input("Masukkan username baru: ")
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
      role = input("Masukkan role karyawan: ").lower()
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
      nama = input("Masukkan nama karyawan yang ingin diedit: ").lower()
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
    if karyawan:
        df = pd.DataFrame(karyawan, columns=["ID", "Nama", "Email", "Nomor Telepon", "Alamat", "Role", "Tanggal Masuk", "Status"])
        df.drop(columns=["ID", "Status"], inplace=True)
        df.index += 1
        print(tb.tabulate(df, headers="keys", tablefmt="psql"))
    else:
        print("Tidak ada karyawan yang aktif.")
    
    input("Tekan Enter untuk kembali")


  def hapusKaryawan():
    run = True
    while run:
      os.system("cls")
      print("=== Hapus Karyawan ===")
      nama = input("Masukkan nama karyawan yang ingin dihapus: ").lower()
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

import os
import view.adminMenu as am
import view.kasirMenu as km
import view.memberMenu as mm
import controller.usersControl as uc
import controller.karyawanControl as kc
import controller.membersControl as mc

def mainMenu():
  while True:
    os.system("cls")
    print("===Bila Cuci Montor==")
    print("1. Admin")
    print("2. Kasir")
    print("3. Member")
    print("0. Exit")
    user = input("Masukkan pilihan :")
    if user == "1":
      admin()
    elif user == "2":
      kasir()
    elif user == "3":
      member()
    elif user == "0":
      os.system("cls")
      break
    else:
      input("Input Tidak sesuai, Enter untuk mengulangi")
      continue

def admin():
  while True:
    os.system("cls")
    print("=== Login Admin ===")
    username = input("Masukkan username :")
    password = input("Masukkan password :")
    list_admin = uc.readAdmin()
    if (username,password) in list_admin:
      am.adminMenu()
    else:
      input("Username atau password tidak sesuai, Enter untuk kembali")
      break

def kasir():
  while True:
    os.system("cls")
    print("=== Login Kasir ===")
    username = input("Masukkan username:")
    password = input("Masukkan password:")
    kasir = input("Masukkan Nama Kasir :")
    list_kasir = []
    for kasir in uc.readKasir():
      if kasir[4] == True:
        list_kasir.append((kasir[1], kasir[2]))
    list_karyawan = []
    for karyawan in kc.read():
      if karyawan[5] == "kasir" and karyawan[7] == True:
        list_karyawan.append(karyawan[1])
    if (username, password) in list_kasir and kasir in list_karyawan:
      km.kasirMenu(kasir)
    elif (username, password) in list_kasir and kasir not in list_karyawan:
      input("Nama kasir tidak sesuai, Enter untuk kembali")
      break
    else:
      input("Username, password atau nama kasir tidak sesuai, Enter untuk kembali")
      break

def member():
  while True:
    os.system("cls")
    print("=== Member Menu ===")
    print("1. Login")
    print("2. Register")
    print("0. Exit")
    user = input("Masukkan pilihan : ")
    if user == "1":
      while True:
        os.system("cls")
        print("=== Login Member ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        list_member = [user[1:3] for user in uc.readMember()]
        if (username, password) in list_member:
          mm.memberMenu(username)
          break
        else:
          input("Username atau password tidak sesuai, Enter untuk mengulangi")
          continue
    elif user == "2":
      run = True
      while run:
        os.system("cls")
        print("=== Register Member ===")
        nama = input("\nMasukkan nama:")
        while run:
          username = input("Masukkan username: ")
          usernames = [user[1] for user in uc.readMember()]
          if username in usernames:
            input("Username telah digunakan, Enter untuk mengulangi")
            continue
          else:
            break
        password = input("Masukkan password: ")
        while run:
          repeatPw = input("Ulangi Password: ")
          if password == repeatPw:
            id_user = uc.addMember(username,password)
            mc.add(id_user,nama)
            input("Akun berhasil dibuat, Enter kembali")
            run = False
          else:
            input("Password tidak sama, Enter untuk mengulangi")
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")
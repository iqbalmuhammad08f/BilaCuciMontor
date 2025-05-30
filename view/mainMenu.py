import os
import view.adminMenu as am
import view.kasirMenu as km
import view.memberMenu as mm
import controller.usersControl as uc

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
    elif user == "2":
      while True:
        os.system("cls")
        print("=== Login Kasir ===")
        username = input("Masukkan username:")
        password = input("Masukkan password:")
        kasir = input("Masukkan Nama Kasir :")
        
    elif user == "3":
      mm.memberMenu()
    elif user == "0":
      os.system("cls")
      break
    else:
      input("Input Tidak sesuai, Enter untuk mengulangi")
      continue



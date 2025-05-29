import os
import controller.usersControl as uc

def memberMenu():
  while True:
    os.system("cls")
    print("=== Member Menu ===")
    print("1. Login")
    print("2. Register")
    print("0. Exit")
    user = input("Masukkan pilihan : ")
    if user == "1":
      print()
    elif user == "2":
      while True:
        os.system("cls")
        print("=== Register Member ===")
        nama = input("\nMasukkan nama:")
        while True:
          username = input("Masukkan username: ")
          usernames = [user[1] for user in uc.read()]
          if usernames == usernames:
            input("Username telah digunakan, Enter untuk mengulangi")
            continue
          else:
            break
        password = input("Masukkan password: ")
        repeatPw = input("Ulangi Password: ")
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")

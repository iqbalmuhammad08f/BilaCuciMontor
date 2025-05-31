import os
import controller.usersControl as uc
import controller.membersControl as mc

def memberMenu():
  run = True
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
      while run:
        os.system("cls")
        print("=== Register Member ===")
        nama = input("\nMasukkan nama:")
        while run:
          username = input("Masukkan username: ")
          usernames = [user[1] for user in uc.read()]
          if usernames in usernames:
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

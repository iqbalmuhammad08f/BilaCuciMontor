import os
import view.memberMenu as memberMenu

def mainMenu():
  while True:
    os.system("cls")
    print("===Bila Cuci Montor==")
    print("1. Login(admin/kasir)")
    print("2. Member")
    print("0. Exit")
    user = input("Masukkan pilihan :")
    if user == "1":
      print()
    elif user == "2":
      memberMenu.memberMenu()
    elif user == "0":
      os.system("cls")
      break
    else:
      input("Input Tidak sesuai, Enter untuk mengulangi")
      continue



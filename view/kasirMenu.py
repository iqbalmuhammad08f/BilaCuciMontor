import os

def kasirMenu(nama_kasir):
  while True:
    os.system("cls")
    print("=== Menu Kasir ===")
    print(f"Selamat datang, {nama_kasir}")
    print("1. Transaksi")
    print("2. Lihat Laporan")
    print("0. Logout")
    user = input("Masukkan pilihan :")
    if user == "1":
      print()
    elif user == "2":
      print()
    elif user == "0":
      break
    else:
      input("Input tidak sesuai, Enter untuk mengulangi")

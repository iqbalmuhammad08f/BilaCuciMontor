import os
import controller.usersControl as uc
import controller.membersControl as mc

def memberMenu():
  while True:
    os.system("cls")
    print("=== Menu Member ===")
    print("1. Pembayaran langanan")
    print("2. Histori")
    print("3. Ubah data diri")
    print("4. Informasi akun")
    print("0. Logout")

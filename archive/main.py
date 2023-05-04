import argparse
import os
from main import *

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="Usage python3 main.py <nama_folder>")
args = parser.parse_args()

if(os.path.isdir(args.nama_folder) == True): 
    print('Selamat datang di program "Manajerial candi"')
    print("Silahkan masukkan username anda")
    

elif(os.path.isdir(args.nama_folder) == False):
    print(f'Folder "{args.nama_folder}" tidak ditemukan.') 


# # Kondisi perintah ga lengkap
# # Masih salah
# elif args.nama_folder is None:
#     parser.error(help)
#     parser.error("Tidak ada nama folder yang diberikan!")
#     parser.error("")
#     parser.error("Usage: python3 main.py <nama_folder>")
#Program utama ada disini
from login import Login
from logout import Logout
from helps import *
import os


role = ""
while True: 
    print(role)
    masukkan = input(">>> ")
    if masukkan == "login" and role == "": 
        while role =="":
            role = Login()
    elif masukkan == "logout": 
        if role != "":
            role = Logout()
        else: 
            print("Anda belum login")
        
    elif role == "jin_pembangun" and masukkan == "bagun": 
        print()
    elif role == "jin_pengumpul" and masukkan == "bruh":
        print()
    elif role == "roro_jonggrang":
        print()
    elif masukkan == "help": 
        print()
    elif masukkan == "exit": 
        exit()

    
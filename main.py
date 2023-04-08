#Program utama ada disini
from F01_Login import Login 
from F02_Logout import Logout
from helps import *


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

    
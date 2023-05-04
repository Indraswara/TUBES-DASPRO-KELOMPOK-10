import csv 
from OurFunction import *
from Z1_ListFunction import *

def ubah_jin(array_of_user : list):
    isUsernameExist = False
    username = input("Masukkkan username Jin: ")
    #check username ada atau tidak 
    i = 0 
    while array_of_user[i] != Mark: 
        if array_of_user[i][0] == username: 
            role = array_of_user[i][2]
            isUsernameExist = True
            break
        i += 1
    if array_of_user[i] == Mark:
        isUsernameExist = False

    #kondisi jika username ditemukan atau tidak
    tipe = ""
    tipe_opposite = ""
    #kondisi jika username ada atau tidak
    if isUsernameExist == True: 
        if role == "jin_pembangun": 
            tipe = "Pembangun"
            tipe_opposite = "Pengumpul"
        elif role == "jin_pengumpul": 
            tipe = "Pengumpul"
            tipe_opposite = "Pembangun"
        #menentukan tipe jin diubah atau tidak
        choice = input(f"Jin ini bertipe {tipe}. Yakin ingin mengubah ke tipe {tipe_opposite} (Y/N)? ")
        #mengubah role dari jin_pembangun ke jin_pengumpul
        if choice == 'Y' and tipe == "Pembangun" and role != "": 
            role = "jin_pengumpul"
        #mengubah role dari jin_pengumpul ke jin_pengumpul
        if choice == 'Y' and tipe == "Pengumpul" and role != "":
            role = "jin_pembangun"
        array_of_user [i][2] = role
    else: 
        print("Tidak ada jin dengan username tersebut")
    return array_of_user

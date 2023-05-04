from Z1_ListFunction import *

def Summonjin(array_of_user : list) -> list: 
    print("Jenis jin yang dapat dipanggil: ")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    while True: 
        role = "jin_pengumpul"
        jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        #jin pengumpul
        if jin == 1: 
            print("memilih jin pengumpul.")
            username = input("Masukkan username jin: ")

            if isUsernameExist(username, array_of_user) == False: 
                while True:
                    password = input("Masukkan password jin: ")
                    if check_password(password) == True: 
                        array_of_user = Appends(array_of_user, [username, password, role, Mark])
                        break
                    else:
                        print("Password panjangnya harus 5-25 karakter!")
                break 
            else: 
                print(f"username {username} sudah diambil")
                      
        #jin pembangun
        elif jin == 2: 
            role = "jin_pembangun"
            print("memilih jin pembangun.")
            username = input("Masukkan username jin: ")
            if isUsernameExist(username, array_of_user) == False: 
                while True:
                    password = input("Masukkan password jin: ")
                    if check_password(password) == True: 
                        array_of_user = Appends(array_of_user, [username, password, role, Mark])
                        break
                    else:
                        print("Password panjangnya harus 5-25 karakter!")
                break 
            else: 
                print(f"username {username} sudah diambil")
            break
        else: 
            print(f"tidak ada jenis jin bernomor {jin}!")
    return array_of_user
       
def isUsernameExist(username : str, array_of_user : list) -> bool: 
    i = 0
    while array_of_user[i] != Mark: 
        if array_of_user[i][0] == username: 
            return True
        i += 1
    return False

def check_password(password : str) -> bool: 
    if len(password) >= 5 and len(password) <= 25: 
        return True
    return False

def summoned_jin(arr : list) -> int: 
    countjin = Len(arr) - 3
    return countjin
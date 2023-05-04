from Z1_ListFunction import *

def HapusJin(array_of_user : list, username_jin : str) -> list: 
    isUsernameExist = False
    #check username ada atau tidak 
    i = 0 
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][0] == username_jin: 
            role = array_of_user[i][2]
            isUsernameExist = True
            break
        i += 1
    
    #kondisi jika username ditemukan atau tidak
    if isUsernameExist == True and (role == 'jin_pengumpul' or role == 'jin_pembangun'): 
        choice = input(f"Apakah anda yakin ingin menghapus jin dengan username {username_jin} Y/N? ")
        if choice == 'Y' or choice == 'y': 
            index = get_element_matriks(array_of_user, username_jin)
            array_of_user = Remove(array_of_user, index)
        elif choice == 'N' or choice == 'n':
            print("Yah gajadi dihapus")
    else: 
        print("Tidak ada jin dengan username tersebut")
    
    return array_of_user

#untuk menghapus jin yang pernah membuat candi 
def HapusJinCandi(array_of_candi : list, username_jin : str) -> list:
    isUsernameExist = False
    #check username ada atau tidak 
    i = 0 
    while array_of_candi[i] != -9999: 
        if array_of_candi[i][1] == username_jin: 
            isUsernameExist = True
            break
        i += 1
    #remove semua yang ada username
    i = 0
    if isUsernameExist == True: 
        while array_of_candi[i] != -9999: 
            array_of_candi[i][0] = str(i)
            if array_of_candi[i][1] == username_jin: 
                array_of_candi = Remove(array_of_candi, i) 
                i = 0
            i += 1
            array_of_candi[0][0] = 'id'


    #kasus jika tidak ada ditemukan jin dengan username_jin
    else: 
        print("Tidak ada jin dengan username tersebut")
    
    return array_of_candi

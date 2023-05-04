from Z1_ListFunction import *
from random import *


def Jin_Pembangun(array_of_candi : list, array_of_material : list, jin_pembangun : str) -> list:
    status_pasir, status_batu, status_air = False, False, False
    pasir = randrange(1,5)
    batu = randrange(1,5)
    air = randrange(1,5)
    if Len(array_of_material) == 1: 
        print("Material tidak cukup")
    else: 
        i = 0
        while Marking(array_of_material[i]) != True: 
            j = 0
            if array_of_material[i][j] == 'pasir': 
                if int(array_of_material[i][2]) < pasir:
                    status_pasir = False
                else:   
                    array_of_material[i][2] = str(int(array_of_material[i][2]) - pasir)
                    status_pasir = True
            elif array_of_material[i][j] == 'batu':
                if int(array_of_material[i][2]) < batu:
                    status_batu = False
                else:   
                    array_of_material[i][2] = str(int(array_of_material[i][2]) - batu)
                    status_batu = True
            elif array_of_material[i][j] == 'air': 
                if int(array_of_material[i][2]) < air:
                    status_air = False
                else:   
                    array_of_material[i][2] = str(int(array_of_material[i][2]) - air)
                    status_air = True
            i += 1
        print(status_air, status_batu, status_pasir)
    if status_air == True and status_batu == True and status_pasir == True: 
        #id;pembuat;pasir;batu;air
        count_candi = Len(array_of_candi)
        print("Candi berhasil dibangun")
        print(f"Sisa candi yang perlu dibangun: {100-count_candi}")
        if count_candi == 101: 
            print("Candi berhasil dibangun")
        else: 
            if Len(array_of_candi) == 1: 
                candi = [str(count_candi), jin_pembangun, str(pasir), str(batu), str(air), Mark]
            else: 
                candi = [str(count_candi), jin_pembangun, str(pasir), str(batu), str(air), Mark]
            Appends(array_of_candi, candi)
    else: 
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")
    return array_of_candi, array_of_material

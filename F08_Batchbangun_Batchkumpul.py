from random import * 
from Z1_ListFunction import *

def Batch_kumpul(array_of_user : list, array_of_material : list) -> list:
    role = "jin_pengumpul"
    i = 0
    count = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == role: 
            count += 1
        i += 1
    pasir, batu, air = 0, 0, 0
    for i in range(count):  
        pasir += randrange(1,5)
        batu += randrange(1,5)
        air += randrange(1,5)

    array_pasir = ['pasir', 'PerluNih!', str(pasir), Mark]
    array_batu = ['batu', 'KerasCuy', str(batu), Mark]
    array_air = ['air', 'Enak nih diminum', str(air), Mark]
    if Len(array_of_material) == 1: 
        array_of_material = Appends(array_of_material, array_pasir)
        array_of_material = Appends(array_of_material, array_batu)
        array_of_material = Appends(array_of_material, array_air)
    else: 
        i = 0
        while Marking(array_of_material[i]) != True: 
            j = 0
            if array_of_material[i][j] == 'pasir': 
                array_of_material[i][2] = str(int(array_of_material[i][2]) + pasir)
            elif array_of_material[i][j] == 'batu':
                array_of_material[i][2] = str(int(array_of_material[i][2]) + batu)
            elif array_of_material[i][j] == 'air': 
                array_of_material[i][2] = str(int(array_of_material[i][2]) + air)
            i += 1
    return array_of_material, pasir, batu, air



def Batch_bangun(array_of_user : list, array_of_candi : list, array_of_material : list) -> list: 
    role = "jin_pembangun"
    i = 0
    count = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == role: 
            count += 1
        i += 1
    #variabel-variabel material
    array_of_material_needed = [None for i in range(count + 1)]
    array_of_material_needed[0] = Mark
    total_pasir_needed = 0
    total_batu_needed = 0
    total_air_needed = 0  

    status_pasir = False
    status_batu = False
    status_air = False
    
    #variabel-variabel jin pembangun
    array_of_jin_pembangun = [None for i in range(count+1)]
    array_of_jin_pembangun[0] = Mark
    i = 0
    while Marking(array_of_user[i]) == False: 
        if array_of_user[i][2] == role: 
            array_of_jin_pembangun = Appends(array_of_jin_pembangun, array_of_user[i][0])
        i += 1

    #Generate banyak bahan 
    for i in range(count): 
        pasir = randrange(1,5)
        batu = randrange(1,5)
        air = randrange(1,5)
        total_pasir_needed += pasir 
        total_batu_needed += batu
        total_air_needed += air
        material_needed = [pasir, batu, air, Mark]
        array_of_material_needed = Appends(array_of_material_needed, material_needed)
    #membandingkan nilai total bahan dibutuhkan dengan total bahan dipunya
    i = 0
    while Marking(array_of_material[i]) != True: 
        if Len(array_of_material) == 1: 
            break
        else: 
            
            if array_of_material[i][0] == 'pasir': 
                if int(array_of_material[i][2]) >= total_pasir_needed:
                    status_pasir = True
            elif array_of_material[i][0] == 'batu':
                if int(array_of_material[i][2]) >= total_batu_needed:  
                    status_batu = True
            elif array_of_material[i][0] == 'air': 
                if int(array_of_material[i][2]) >= total_air_needed:
                    status_air = True
        i += 1
    #jika kasus semua bahan cukup
    if status_air == True and status_batu == True and status_pasir == True: 
        #mengurangi bahan
        for i in range(count): 
            pasir_needed = array_of_material_needed[i][0]
            batu_needed = array_of_material_needed[i][1]
            air_needed = array_of_material_needed[i][2]
            j = 0
            while Marking(array_of_material[j]) != True:
                if array_of_material[j][0] == 'pasir': 
                    pasir_have = int(array_of_material[1][2])
                    (array_of_material[j][2]) = str(pasir_have - pasir_needed)
                elif array_of_material[j][0] == 'batu':
                    batu_have = int(array_of_material[2][2])
                    array_of_material[j][2] = str( batu_have - batu_needed)
                elif array_of_material[j][0] == 'air': 
                    air_have = int(array_of_material[3][2]) 
                    array_of_material[j][2] = str( air_have - air_needed)
                j += 1 
                #membangun candi
            count_candi = Len(array_of_candi)
            print("Candi berhasil dibangun")
            print(f"Sisa candi yang perlu dibangun: {100-count_candi}")
            if count_candi == 101: 
                print("Candi berhasil dibangun")
            else: 
                if Len(array_of_candi) == 1: 
                    candi = [str(count_candi), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                else: 
                    candi = [str(count_candi), array_of_jin_pembangun[i], str(pasir_needed), str(batu_needed), str(air_needed), Mark]
                Appends(array_of_candi, candi)
        status_bangun = True
        return array_of_material, array_of_candi, count, total_pasir_needed, total_batu_needed, total_air_needed, status_bangun
    
    #kasus bahan tidak mencukupi
    else:
        status_bangun = False
        if count == 0: 
            return array_of_material, array_of_candi, count, total_air_needed, total_batu_needed, total_air_needed, status_bangun
        else: 
            j = 0
            while Marking(array_of_material[j]) != True:
                if array_of_material[j][0] == 'pasir':
                    pasir_have = int(array_of_material[j][2])
                elif array_of_material[j][0] == 'batu':
                    batu_have = int(array_of_material[j][2])
                elif array_of_material[j][0] == 'air': 
                    air_have = int(array_of_material[j][2]) 
                j += 1

            pasir_needed = pasir_have - total_pasir_needed
            batu_needed = batu_have - total_batu_needed
            air_needed = air_have - total_air_needed
            return array_of_material, array_of_candi, count, pasir_needed, batu_needed, air_needed, status_bangun
    
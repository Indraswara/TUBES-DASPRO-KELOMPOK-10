#Tanpa bonus 
from random import *
from Z1_ListFunction import *

def CollectMaterial(array_of_material : list) -> list:
    pasir = randrange(1,5)
    batu = randrange(1,5)
    air = randrange(1,5)
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
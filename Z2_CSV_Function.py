from Z1_ListFunction import * 


def split_csv(line: str) -> list: 
    Appened_Array = [None for i in range(Neff)]
    Appened_Array[0] = Mark
    string = ""
    for i in range(len(line)): 
        if line[i] != ';' and line[i] != '\n' and line[i] !='': 
            string += line[i]
        else: 
            Appened_Array = Appends(Appened_Array, string)
            string = ""
    if string != "":
        Appened_Array = Appends(Appened_Array, string)
    return Appened_Array


# kalo boleh f.readlines()
def matriks_csv(arr : list, list_item) -> list: 
    arr[0] = Mark
    for item in list_item: 
        temp = split_csv(item)
        arr = Appends(arr, array_eff_None(temp))
    return arr

# kalo bolehnya f.readline()
def matriks_csv2(arr : list, line) -> list: 
    arr[0] = Mark
    temp = ""
    for i in range(len(line)): 
        temp += line[i]
        if line[i] == '\n': 
            temp_array = split_csv(temp)
            arr = Appends(arr, array_eff_None(temp_array))
            temp = ""
    return arr

## penggunaan split 
    """array = [None for i in range(Neff)]
    array[0] = Mark
    for item in a: 
        temp = split_csv(item)
        array = Appends(array, array_eff_None(temp))"""
    #array = Appends(array, temp)
##debuggingS
"""    array = array_eff_None(array)
    print(array)"""


"""def csv_to_array(string : str) -> list: 
    newarr = [None for i in range(Neff)]
    newarr[0] = Mark
    temp = ""
    for i in range(len(string)): 
        if string[i] != ';' and string[i] != '\n' and string[i] != '':  
            temp += string[i]
        else: 
            newarr = Appends(newarr, temp)
            temp = ""
    if string != "":
        newarr = Appends(newarr, temp)
    return newarr
    """
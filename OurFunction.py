#pengganti fungsi append()
def appends(array, a, Length): 
    newarr = [0 for i in range(Length + 1)]
    for i in range(Length + 1): 
        if i != Length:
            newarr[i] = array[i]
        else: 
            newarr[i] = a
    return newarr

#pengganti fungsi pop()
def pops(array, a, Length): 
    newarr = []
    for i in range(Length): 
        if i != a: 
            newarr = appends(newarr, array[i], Length)
    return newarr

#pengganti fungsi len()
def Len(array):
    stringS = ""
    i = 0
    status = True
    while status: 
        stringS += array[i]
        i += 1
        if stringS == array: 
            status = False
    return i 

#pengganti fungsi sort 
def sorts(array, Length): 
    for i in range(Length): 
        for j in range(0, Length-i-1): 
            if array[j] > array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j]
    return array

#pengganti fungsi split()
def splits(arr, b, Length): 
    newarr = []
    bruh = newarr
    a = ""
    for i in range(Length): 
        if arr[i] == b: 
            newarr = appends(newarr, a, Length)
            a = ""
        else: 
            a += arr[i]
    newarr = appends(newarr, a, Length)
    if bruh == newarr:
        return newarr
    else: 
        return arr


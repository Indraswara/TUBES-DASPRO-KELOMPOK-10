def Length(array):
    arrays = ""
    i = 0
    while True: 
        arrays += str(array[i])
        i += 1
        if arrays == array: 
            break

    return i

a = "kontol"
print(Length(a))

def my_len(arr): 
    # inisialisasi variabel counter dan index
    counter = 0
    index = 0
    
    # loop while dengan kondisi index tidak melebihi panjang array
    while index < arr.__sizeof__() / arr[0].__sizeof__():
        # cek apakah nilai pada indeks saat ini None
        if arr[index] is None:
            # jika ya, maka panjang array telah ditemukan, keluar dari loop
            break
        else:
            # jika tidak, tambahkan counter dan indeks sebanyak 1
            counter += 1
            index += 1
    
    # kembalikan nilai counter
    return counter

a = "cok"
print(my_len(a))

def get_array_length(arr):
    if arr == []:
        return 0
    mark = object()
    i = 0
    while arr and arr[i] is not mark:
        arr[i], mark = mark, arr[i]
        i += 1
    return i
a = [1,2,4,4]
print(get_array_length(a))

def hitung_panjang(arr):
    count = 0
    while arr:
        count += 1
        arr = arr[1:]
    return count
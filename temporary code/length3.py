
def Len(array):
    last = -1
    array = list(array)
    if array == []: 
        return 0
    else: 
        array[last] = "mark"
        count = 0
        while array[count] != "mark": 
            count += 1
        count += 1
        return count
arr = [1,2,3,4,5]
print(Len(arr))
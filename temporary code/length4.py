
fixed_size = 1000
def Len(array):
    arr = [None for i in range(fixed_size)]
    a = list(array)
    if a == []: 
        return 0
    else: 
        i = 0
        while a[i] != None: 
            arr[i] = array[i]
            i+=1 
                
        return i
  
arr = [1,2,3,4,5]
print(Len(arr))
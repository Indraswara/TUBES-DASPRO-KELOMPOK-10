import os 
from Z1_ListFunction import *

def save(path : str,  arr : list, namefile: str):
    if not os.path.exists(path):
        print("ga ada foldernya")
        os.makedirs(path)
        f = open(os.path.join(path, namefile), 'w')
        f.close()
        f = open(os.path.join(path, namefile), 'w')
        i = 0
        while arr[i] != Mark:
            j = 0
            while arr[i][j] != Mark:
                if arr[i][j+1] == Mark:
                    f.write(f"{arr[i][j]}")
                    break
                f.write(f"{arr[i][j]};")
                j += 1
            f.write("\n")
            i += 1
        f.close()

    else:
        f =  open(os.path.join(path, namefile), 'w')
        f.close()
        i = 0
        f = open(os.path.join(path, namefile), 'w')
        while arr[i] != Mark: 
            j = 0
            while arr[i][j] != Mark:
                if arr[i][j+1] == Mark:
                    f.write(f"{arr[i][j]}")
                    break
                f.write(f"{arr[i][j]};")
                j += 1
            f.write("\n")
            i += 1
        f.close()

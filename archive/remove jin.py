i = 0
            #jika ada jin dengan username maka username tersebut dihapus
    while array_of_user[i] != -9999: 
        if array_of_user[i][1] == username_jin:   
            array_of_user = Remove(array_of_user, i)
                break
        i += 1
import csv 
from OurFunction import *


def Login():
    login_status = False
    not_found = False
    f = open('user.csv', 'r+')
    reader = csv.reader(f, delimiter=";")

    username = input("Username: ")
    password = input("Password: ")
    
    #check username ada atau tidak
    username_check = []
    for row in reader: 
        username_check = appends(username_check,row[0])
        if row[0] == username and row[1] == password: 
                login_status = True
                role = row[2]

    for i in range(Length(username_check)): 
        if username == username_check[i] : 
            not_found = False
            break
        else: 
            not_found = True

    if not_found == True: 
        print("username tidak terdaftar")
        role = ""
        return role
    else:
        if login_status == False: 
            print("Password salah!")
            role = ""
            return role
        else: 
            print(f"Selamat datang {username}")
            return role

import os 
import pandas as pd

def clear_screen():
    os.system("clear")


def staff_login():
    password = "pawsadopt2024"
    login = False
    count = 0
    while (login == False):
        count += 1
        attempt = input("Enter password:")
        if attempt == password:
            login = True
            print("Correct Password. Staff Options:")
            staff_options()
            os
        else:
            print("Incorrect Password, Try again!")

def staff_options():
    choice = "0"
    while choice != "6":
        print("1. Add New Pet")
        print("2. Complete an Adoption")
        print("3. View All Pets (including adopted)")
        print("4. View Statistics")
        print("5. Remove a Pet")
        print("6. Logout")
        choice = input("Choose from one of the above:")
        if choice == "3":
            #df = pd.read_csv("pets.csv")
            #print(df.to_string())
            print("")
            print("Returned to Staff Options")
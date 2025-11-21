#import os 
import pandas as pd
import viewing

    #os.system("clear")


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
        if choice == "1":
            viewing.add_pet()
        if choice == "3":
            viewing.read_pet_staff()
            print("")
            print("Returned to Staff Options")
        if choice == "5":
            viewing.remove_pet()


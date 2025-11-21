import staff
import pandas as pd 

def adopter_login():
    df = pd.read_csv("adopters.csv")
    adopter_id = input("What is your ID:")
    if len(adopter_id) == 4:
        df = df[df["AdopterID"]== adopter_id]
    if len(df) == 1:
        print("Login Successful. Adopter Menu:")
        adopter_menu()
    else:
        print("Login failed")

def adopter_menu(): 
    choice = "0"
    while choice != "5":
        print("1. View My Compatibility Matches")
        print("2. Reserve a Pet")
        print("3. View My Reserved/Adopted Pets")
        print("4. Cancel a Reservation")
        print("6. Logout")
        choice = input("Choose from the above")






    



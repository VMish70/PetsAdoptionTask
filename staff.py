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

def complete_adoption():
    df = pd.read_csv("pets.csv")
    filter_df = df[df["Status"]=="Reserved"]
    if len(filter_df) == 0:
        print("None currently!")
        return 
    adopted_petID = input("Give the ID of the pet that is going to be adopted:")
    adopted_df = filter_df[filter_df["PetID"]== adopted_petID]
    if len(adopted_df) != 0:
        adopter_df = pd.read_csv("adopters.csv")
        adopter_df = adopter_df[adopter_df["AdoptedPets"]==adopted_petID]
        print(adopted_df)
        print(adopter_df)
        adoption_choice = input("Confirm Adoption completion: Yes or No")
        if adoption_choice == "Yes":
            

    
complete_adoption()
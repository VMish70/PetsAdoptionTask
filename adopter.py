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
        if choice == "2":
            reserve_pet()

def reserve_pet():
    df = pd.read_csv("adopters.csv")
    filter_df =df[df["AdoptedPets"]=="None"]
    if len(filter_df) == 0:
        print("You already have a reservation. Please complete or cancel it first.")
        pass
    print(filter_df)
    adopter_choice = input("Enter the Pet ID of the pet you want to reserve:")



def register_adopter():
    df = pd.read_csv("adopters.csv")
    num_row = str(len(df))
    adopter_ID = "A" + num_row.zfill(3)
    adopter_name = input("Enter your name: (Note must be only 2 words!)")
    adopter_home = input("Home type (Flat, House, or Farm only)")
    adopter_experience = input("Experience level (None, Some, or Expert)")
    adopter_pet_size = input("Preferred pet size (Small, Medium, Large, or Any)")
    adopter_energy = input("Preferred energy level (Low, Medium, High, or Any)")
    if len(adopter_name.split(" ")) >=2 :
        adopter_pets = "None"
        df.loc[len(df)] = [adopter_ID,adopter_name, adopter_home, adopter_experience, adopter_pet_size, adopter_energy, adopter_pets]
        df.to_csv("adopters.csv", index = False)
        print(df)
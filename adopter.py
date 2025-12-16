
import pandas as pd 
import os
g_adopter_id = 0
def adopter_login():
    global g_adopter_id
    df = pd.read_csv("adopters.csv")
    adopter_id = input("What is your ID:")
    g_adopter_id = adopter_id
    if len(adopter_id) == 4:
        df = df[df["AdopterID"]== adopter_id]
    if len(df) == 1:
        print("Login Successful. Adopter Menu:")
        adopter_menu()
    else:
        print("Login failed")
def register_adopter():
    df = pd.read_csv("adopters.csv")
    num_row = str(len(df)+1)
    adopter_ID = "A" + num_row.zfill(3)
    for i in range(3):
        adopter_name = input("Enter your name: (Note must be only 2 words!)")
        adopter_home = input("Home type (Flat, House, or Farm only)")
        adopter_experience = input("Experience level (None, Some, or Expert)")
        adopter_pet_size = input("Preferred pet size (Small, Medium, Large, or Any)")
        adopter_energy = input("Preferred energy level (Low, Medium, High, or Any)")
        if len(adopter_name.split(" ")) >=2 :
            if adopter_home == "Flat" or adopter_home == "House" or adopter_home == "Farm":
                if adopter_experience == "None" or adopter_experience == "Some" or adopter_experience == "Expert":
                    if adopter_pet_size == "Small" or adopter_pet_size == "Medium" or adopter_pet_size == "Large" or adopter_pet_size == "Any":
                        if adopter_energy == "Low" or adopter_energy == "Medium" or adopter_energy == "High" or adopter_energy == "Any":
                            adopter_pets = "None"
                            df.loc[len(df)] = [adopter_ID,adopter_name, adopter_home, adopter_experience, adopter_pet_size, adopter_energy, adopter_pets]
                            df.to_csv("adopters.csv", index = False)
                            print(df)
        else:
            print("Fill in the correct parameters!")
    os.system("clear")
    print("Failed too many times! Returned to main menu.")

    

def adopter_menu(): 
    choice = "0"
    while choice != "5":
        print("1. View My Compatibility Matches")
        print("2. Reserve a Pet")
        print("3. View My Reserved/Adopted Pets")
        print("4. Cancel a Reservation")
        print("5. Logout")
        choice = input("Choose from the above: ")
        if choice == "1":
            os.system("clear")
            compatibility_match()
        if choice == "2":
            os.system("clear")
            reserve_pet()
        if choice == "4":
            os.system("clear")
            cancel_reservation()
        if choice >= "5":
            os.system("clear")
            print("Returned to Main Menu:")
            return

    
filter_df = 0
def compatibility_match():
    df=pd.read_csv("pets.csv")
    df_adopter = pd.read_csv("adopters.csv")
    #get available pets
    df=df[df['Status']=='Available']
    points=0
    df_adopter = df_adopter[df_adopter["AdopterID"]== g_adopter_id]
    home=df_adopter.iloc[0]["HomeType"]
    prefered_size=df_adopter.iloc[0]["PreferredSize"]
    prefered_energy=df_adopter.iloc[0]["PreferredEnergy"]
    adopter_experience = df_adopter.iloc[0]["Experience"]
    pet_energy = df.iloc[0]["Energy"]
    pet_age = df.iloc [0]["Age"]
    compatibility_rating=0
    print("Home is ", home)
    print("Prefered size", prefered_size)
    print("Energy",prefered_energy)
    df_with_score=pd.DataFrame(columns=['PetID', 'Score', 'Rating'])
    for i, r in df.iterrows():
        points=0
        #Home Type Match
        if r["Type"]=="Dog" and r["Size"]=="Large" and home=="Flat":
            points=points-20
        if r["Type"]=="Dog" and home=="Farm":
            points=points+15
        if (r["Type"]=="Rabbit" or r["Type"]=="Cat" or r["Type"]=="Hamster") and home=="Flat":
            points=points+10
        
        # Size Preference match
        if prefered_size==r["Size"]:
            points=points+20
        if prefered_size=="Any":
            points=points+10
        
        #Energy level match
        if r["Energy"]==prefered_energy:
            points=points+20
        if prefered_energy=="Any":
            points=points+10


        #Experience Bonus
        if adopter_experience == "Expert":
            points = points + 15
        if adopter_experience == "Some":
            points = points + 10
        elif pet_energy == "High" and adopter_experience == "None":
            points = points - 15 

        #Age Consideration
        if pet_age >= 6:
            points = points + 10

        
        #Calculate compatibility rating
        if(points >=50):
            compatibility_rating= "Excellent Match! 3 stars"
        if(points>=30 and points<50) :
            compatibility_rating= "Good Match! 2 stars"
        if(points>=10 and points<30):
            compatibility_rating= "Possible Match! 1 star"
        if(points<10):
            compatibility_rating= "Not recommended! 0 star"
        global filter_df
        df_with_score.loc[i]=[r["PetID"], points, compatibility_rating]
        filter_df = df_with_score.sort_values("Score", ascending = False)
    print("Now showing scores:") 
    print(filter_df)

def cancel_reservation():
    df = pd.read_csv("pets.csv")
    adopter_df = pd.read_csv("adopters.csv")
    filter_df = df[df["Status"]=="Reserved"]
    if len(filter_df) == 0:
        print("No pet")
        adopter_menu()
    cancel_petID = input("Give the PetID of the pet yoy want to cancel the reservation of:")
    no_reserve_df = filter_df[filter_df["PetID"] == cancel_petID]
    confirmation = input("Confirm Cancelation: Yes or no!")
    if len(no_reserve_df) == 1:
        if confirmation == "Yes":     
            no_reserve_df = no_reserve_df[no_reserve_df["PetID"] == "Available"]
            adopter_df = adopter_df[adopter_df["AdoptedPets"]== cancel_petID]
            adopter_df = adopter_df[adopter_df["AdoptedPets"]== "None"]
        else:
            print("returned to Adopter Menu:")
            adopter_menu()


def reserve_pet():
    df = pd.read_csv("adopters.csv")
    filter_df =df[df["AdoptedPets"]=="None"]
    if len(filter_df) == 0:
        print("You already have a reservation. Please complete or cancel it first.")
        pass
    print(filter_df)
    adopter_choice = input("Enter the Pet ID of the pet you want to reserve:")
    adopted_df = filter_df[filter_df["PetID"]== adopter_choice]
    available_adopted_df = adopted_df[adopted_df["Status"] == "Available"]
    if len(available_adopted_df) == 0:
        print("No available pet!")
        adopter_menu()
    elif filter_df[filter_df["Score"] <= 10]:
        confirmation = input("Warning: This pet's compatibility score is low. Are you sure? (Yes/No)")
        if confirmation == "No":
            print("Returned to Adopter Menu:")
            adopter_menu()
        else:
            available_adopted_df = adopted_df[adopted_df["Status"] == "Reserved"]
            base_fee =- available_adopted_df.iloc[adopter_choice]["Fee"]
            if df[df["DaysInCentre"]== 60]:
                fee = float(base_fee * 0.7)

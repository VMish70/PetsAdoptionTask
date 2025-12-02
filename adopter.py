
import pandas as pd 

def adopter_login():
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
g_adopter_id = None
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
            compatibility_match()
        if choice == "2":
            reserve_pet()
        if choice >= "5":
            return

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
    num_row = str(len(df)+1)
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

def compatibility_match():
    df=pd.read_csv("pets.csv")
    df_adopter = pd.read_csv("adopters.csv")
    #get available pets
    df=df[df['Status']=='Available']
    points=0
    ##adopter_login_id= df_adopter[df_adopter["AdopterID"]== g_adopter_id]
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


    df_with_score=pd.DataFrame(columns=['PetId', 'Score', 'Rating'])


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


    df_with_score.loc[i]=[r["PetID"], points, compatibility_rating]


    print("Now showing scores:") 
    for i,r in df_with_score.iterrows():
        print(df_with_score)
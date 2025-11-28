import pandas as pd
def read_pet():
    df = pd.read_csv("pets.csv")
    filter_df =df[df["Status"]=="Available"]
    filter_df = filter_df.sort_values("DaysInCentre", ascending = False)
    print(filter_df)
    print("The average days in centre for all pets is:")
    print(filter_df["DaysInCentre"].sum()/len(filter_df))


def read_pet_staff():
    df = pd.read_csv("pets.csv")
    print(df)

def add_pet():
    df = pd.read_csv("pets.csv")
    num_row = str(len(df))
    petID = "P" + num_row.zfill(3)
    petName = input("What's the name of the pet:")
    petType = input("What animal is this pet:")
    petAge = int(input("What age is this pet. must be 0-20:"))
    petSize = input("What size? Small, Medium or Large:")
    petEnergy = input("What's the energy. Low, Medium, or High")
    petFee = int(input("What's the adoption fee between £20 - £300"))
    petStatus = "Available"
    petDays = 0
    df.loc[len(df)] = [petID, petName, petType, petAge, petSize, petEnergy, petFee, petStatus, petDays]
    df.to_csv("pets.csv", index = False)
    print(df)

def remove_pet():
    df = pd.read_csv("pets.csv")
    print(df)
    remove = input("Enter ID to remove")
    df.set_index("PetID")
    df.drop(remove)
    df.to_csv("pets.csv")
    print(df)
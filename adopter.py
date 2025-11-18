import staff
import pandas as pd 

def adopter_login():
    df = pd.read_csv("adopters.csv")
    adopter_id = input("What is your ID:")
    if len(adopter_id) == 4:
        df = df[df["AdopterID"]= adopter_id]
    if len(df) == 1:
        print("Login Successful. Adopter Menu")
    else:
        print("Login failed")

    
adopter_login()

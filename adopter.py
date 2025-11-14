import staff

def adopter_login():
    adopter_id = input("What is your ID:")
    if adopter_id in staff.df.adopters.csv:
        id = staff.df[staff.df.adopter.csv == adopter_id]

adopter_login()
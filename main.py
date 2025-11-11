import staff 
import viewing
def main_menu():
    choice = "0"
    while choice != "5":
        
        print("1. View Available Pets")
        print("2. Register as New Adopter")
        print("3. Adopter Login")
        print("4. Staff Menu")
        print("5. Quit")
        choice = input("Choose from one of the above:")
        if choice == "1":
            viewing.read_pet()
        if choice == "4":
            staff.staff_login()

main_menu()
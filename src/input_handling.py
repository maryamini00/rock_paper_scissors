from email_validator import validate_email, EmailNotValidError
from utils import exit_program
from user_class import user
from output_handling import user_information
def user_info():
    name = input("name : ")
    while True:
        email = input("email : ")
        try:
            email_info = validate_email(email, check_deliverability=True)
            email = email_info.normalized
            return(name, email)
        
        except EmailNotValidError as e:
            print("invalid email\ntry again !")
            

def start_game():
    print("Hit the Enter key so we can start the game :)))")
    while True:
        i = input().lower()
        if i == "e" or i =="exit":
            exit_program()
        elif i == "":
            break
        else:
            print("\ninvalid input")
            print("try again !\n")
    
def play_exit(start_end_choice_print):
    while True:
        start_end_choice_print
        i = input("your choice : ").lower()
        if i == "e" or i =="exit":
            exit_program()
        elif i == "p" or i == "profile":
            if user.email == "":
                print("You haven't created a profile yet.")
                print("if you want to create a profile inter s")
            else:
                user_information()
                user.print_profile()
        elif i == "s" or i == "start":
            break
        else:
            print("\ninvalid input")
            print("try again !\n")
            
def input_123_with_validation():
    while True:
        i = input("     your choice : ")
        if i == '1' or i == '2' or i == '3':
            return int(i) 
        else:
            print("\n     invalid input")
            print("     try again !\n")


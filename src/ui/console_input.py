from email_validator import validate_email, EmailNotValidError
from ui.console_output import exit_print
import sys
def user_info():
    name = input("name : ")
    while True:
        email = input("email : ")
        try:
            email_info = validate_email(email, check_deliverability=False)
            email = email_info.normalized
            return(name, email)
        
        except EmailNotValidError as e:
            print("invalid email\ntry again !")
            

def start_game():
    print("\n the Enter key so we can start the game :)))")
    while True:
        i = input().lower()
        if i == "e" or i =="exit":
            exit_print()
            sys.exit()
        elif i == "":
            break
        else:
            print("\ninvalid input")
            print("try again !\n")
    
def menu_choice():
    while True:
        i = input("your choice : ").lower()
        if i in ("e", "exit"):
            return "exit"
        elif i in ("p", "profile"):
            return "profile"
        elif i in ("s", "start"):
            return "start"
        print("\ninvalid input\ntry again !\n")
            
def input_123_with_validation():
    while True:
        i = input("    your choice : ")
        if i == '1' or i == '2' or i == '3':
            return int(i) 
        else:
            print("\n    invalid input")
            print("    try again !\n")


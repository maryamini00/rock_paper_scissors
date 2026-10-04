import output_handling as output 
import input_handling as input
import user_class as uc
def main():
    output.game_title()
    print("\nfirst than first input your information")
    name, email = input.user_info()
    uc.user.change_name(name)
    uc.user.change_email(email)
    while True:
        input.play_exit(output.start_end_choice())
        output.start_game()
        
        
        
        exit()
    #     for i in range(7):
        
    

if __name__ == "__main__":
    main()

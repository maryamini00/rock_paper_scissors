import output_handling as output 
import input_handling as input
import user_class as uc
import computer_class as cc
from utils import reviewing_input_logic, reviewing_result
def main():
    output.program_title()
    print("\nfirst than first input your information")
    name, email = input.user_info()
    uc.user.change_name(name)
    uc.user.change_email(email)
    while True:
        input.play_exit(output.start_end_choice())
        output.start_game()
        output.finding_person()
        output.user_information()
        cc.computer_user.print_profile()
        input.start_game()
        output.game_logic()
        comp_score = 0 
        user_score = 0
        for i in range(7):
            output.game_title(i)
            output.each_round_game()
            user_choice = input.input_123_with_validation()
            computer_choice = cc.computer_random_choice()
            comp_score_add, user_score_add = reviewing_result(reviewing_input_logic(computer_choice, user_choice))
            comp_score = comp_score + comp_score_add
            user_score = user_score + user_score_add
            print("|    computer input : ", computer_choice, "                         |")
            print("|    Result :                                     |")
            print("|    Computer : ", comp_score, "                               |")
            print("|    User : ", user_score, "                                   |")
            print("---------------------------------------------------")
        
        exit()
    #     for i in range(7):
        
    

if __name__ == "__main__":
    main()

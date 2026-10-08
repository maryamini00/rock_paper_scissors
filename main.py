import src.ui.console_output as oh
import src.ui.console_input as ih
from src.models.player import Player
import src.services.opponent as cc
from src.rules import reviewing_input_logic, reviewing_result_each_round, Reviewing_overall_result
from src.game import exit_program

user = Player("", "", 0, 0)
def main():
    print("\n")
    oh.program_title()
    print("\nfirst than first input your information")
    name, email = ih.user_info()
    user.change_name(name)
    user.change_email(email)
    while True:
        while True:
            oh.start_end_choice()
            choice = ih.menu_choice()
            if choice == "exit":
                exit_program()
            elif choice == "profile":
                oh.user_information()
                user.print_profile()
                continue
            break
        oh.start_game()
        oh.finding_person()
        computer = cc.create_computer_player()
        oh.user_information()
        computer.print_profile()
        ih.start_game()
        oh.game_logic()
        comp_score = 0 
        user_score = 0
        for i in range(7):
            oh.game_title(i)
            oh.each_round_game()
            user_choice = ih.input_123_with_validation()
            computer_choice = cc.computer_random_choice()
            comp_score_add, user_score_add = reviewing_result_each_round(reviewing_input_logic(computer_choice, user_choice))
            comp_score = comp_score + comp_score_add
            user_score = user_score + user_score_add
            oh.continuation_each_round_game(computer_choice, comp_score, user_score)
        oh.result_title()
        print(Reviewing_overall_result(comp_score, user_score, computer.add_loss, computer.add_win, user.add_loss, user.add_win))
        
    exit()

if __name__ == "__main__":
    main()

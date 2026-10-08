import ui.console_output as co
import ui.console_input as ci
from models.player import Player
import services.opponent as op
from rules import reviewing_input_logic, reviewing_result_each_round, Reviewing_overall_result
from game import exit_program

user = Player("", "", 0, 0)
def main():
    print("\n")
    co.program_title()
    print("\nfirst than first input your information")
    name, email = ci.user_info()
    user.change_name(name)
    user.change_email(email)
    while True:
        while True:
            co.start_end_choice()
            choice = ci.menu_choice()
            if choice == "exit":
                exit_program()
            elif choice == "profile":
                co.user_information()
                user.print_profile()
                continue
            break
        co.start_game()
        co.finding_person()
        computer = op.create_computer_player()
        co.user_information()
        computer.print_profile()
        ci.start_game()
        co.game_logic()
        comp_score = 0 
        user_score = 0
        for i in range(7):
            co.game_title(i)
            co.each_round_game()
            user_choice = ci.input_123_with_validation()
            computer_choice = op.computer_random_choice()
            comp_score_add, user_score_add = reviewing_result_each_round(reviewing_input_logic(computer_choice, user_choice))
            comp_score = comp_score + comp_score_add
            user_score = user_score + user_score_add
            co.continuation_each_round_game(computer_choice, comp_score, user_score)
        co.result_title()
        print(Reviewing_overall_result(comp_score, user_score, user.add_loss, user.add_win))     
    exit()

if __name__ == "__main__":
    main()

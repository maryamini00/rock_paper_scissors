import ui.console_output as co
import ui.console_input as ci
from models.player import Player
import services.opponent as op
from game import play_game
import sys

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
                co.exit_print()
                sys.exit()
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
        co.result(play_game(ci, co, user.add_loss, user.add_win))

if __name__ == "__main__":
    main()

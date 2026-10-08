from rules import round_winner, round_points, overall_winner
import services.opponent as op

def play_game(ci, co, user_add_loss, user_add_win, rounds=7):
    comp_score = 0
    user_score = 0
    for i in range(rounds):
        co.game_title(i)
        co.each_round_game()
        user_choice = ci.input_123_with_validation()
        comp_choice = op.computer_random_choice()

        winner = round_winner(comp_choice, user_choice)
        comp_add, user_add = round_points(winner)
        comp_score += comp_add
        user_score += user_add
        co.continuation_each_round_game(comp_choice, comp_score, user_score)
    return overall_winner(comp_score, user_score, user_add_loss, user_add_win)

def record_result(winner, user, computer):
    if winner == "user":
        user.add_win()
    elif winner == "computer":
        user.add_loss()
    
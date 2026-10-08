def round_winner(comp_choice, user_choice):
    try:
        if comp_choice == user_choice:
            return "both"
        elif comp_choice == 1 and user_choice == 2:
            return "user"
        elif comp_choice == 2 and user_choice == 1:
            return "computer"
        elif comp_choice == 1 and user_choice == 3:
            return "computer"
        elif comp_choice == 3 and user_choice == 1:
            return "user"
        elif comp_choice == 3 and user_choice == 2:
            return "computer"
        elif comp_choice == 2 and user_choice == 3:
            return "user"
        else:
            return "invalid"
    except:
        return "ERROR"
    
def round_points(winner):
    """first computer score and second user score"""
    if winner == "both":
        return 1, 1
    elif winner == "user":
        return 0, 1
    elif winner == "computer":
        return 1, 0
    else:
        return 0, 0

def overall_winner(comp_score, user_score, user_add_loss, user_add_win):
    if comp_score > user_score:
        user_add_loss()
        return "Computer is winner :(\n"
    elif user_score > comp_score:
        user_add_win()
        return "You are winner :)\n"
    else:
        return "Draw :)\n"
    

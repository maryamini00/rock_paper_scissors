def exit_program():
    print("\ncome back later and let's play together again.")
    print("I'll be waiting for you.")
    print("\nexiting the program...")
    exit()
    
def reviewing_input_logic(comp_choice, user_choice):
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
    
def reviewing_result(i):
    if i == "both":
        comp_score = 1
        user_score = 1
        return comp_score, user_score
    elif i == "user":
        comp_score = 0
        user_score = 1
        return comp_score, user_score
    elif i == "computer":
        comp_score = 1
        user_score = 0
        return comp_score, user_score
    else:
        comp_score = 0
        user_score = 0
        return comp_score, user_score


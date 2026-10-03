class Player:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.score = 0
        self.losses = 0
        self.wins = 0

    def increase_score(self):
        self.score += 1
    def decrease_score(self):
        self.score -= 1
    def print_score(self):
        print("your score: ", self.score)  
        
    def change_name(self, new_name):
        self.name = new_name
    def change_email(self, new_email):
        self.email = new_email
        
    def add_win(self):
        self.wins += 1
    def add_loss(self):
        self.losses += 1
    
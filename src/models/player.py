class Player:
    def __init__(self, name, email, losses, wins):
        self.name = name
        self.email = email
        self.losses = losses
        self.wins = wins
        
    def change_name(self, new_name):
        self.name = new_name
    def change_email(self, new_email):
        self.email = new_email
        
    def add_win(self):
        self.wins += 1
    def add_loss(self):
        self.losses += 1
        
    def print_profile(self):
        print("Name : ", self.name)
        print("Email : ", self.email)
        print("Wins : ", self.wins)
        print("Losses : ", self.losses)
    
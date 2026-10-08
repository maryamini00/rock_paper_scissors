from models.player import Player
from faker import Faker as fk
import numpy as np
fake = fk()
def create_computer_player():
    return Player(fake.name(), fake.email(), np.random.randint(1, 60), np.random.randint(1, 60))

def computer_random_choice():
    return np.random.randint(1, 4)
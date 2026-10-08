from models.player import Player
import random
from faker import Faker as fk
fake = fk()

def create_computer_player():
    return Player(fake.name(), fake.email(), random.randint(1, 60), random.randint(1, 60))

def computer_random_choice():
    return random.randint(1, 3)
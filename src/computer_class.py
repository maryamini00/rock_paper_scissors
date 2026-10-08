from class_structure import Player
from faker import Faker as fk
import numpy as np
fake = fk("fa_IR")

computer_user = Player(fake.name(), fake.email(), np.random.randint(1, 60), np.random.randint(1, 60))

def computer_random_choice():
    return np.random.randint(1, 4)
from class_structure import Player
from faker import Faker as fk
fake = fk("fa_IR")

computer_user = Player(fake.name(), fake.email())
import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
value = roll_dice()
print(f"You rolled a {value}.")

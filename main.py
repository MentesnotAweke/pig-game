import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
value = roll_dice()
print(f"You rolled a {value}.")

players = input("Enter the number of players (1-4):")
if players.isdigit():
    players = int(players)
    if 1 <= players <= 4:
        print(f"Starting the game with {players} player(s).")
        # Here you can add more game logic based on the number of players
        # For example, initializing player scores, etc.
        for player in range(1, players + 1):
            print(f"Player {player}'s turn.")
            # Simulate a turn for each player
            roll = roll_dice()
            print(f"Player {player} rolled a {roll}.")
    else:
        print("Please enter a number between 1 and 4.")
else:
    print("Invalid input. Please enter a number between 1 and 4.")
import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
while True:
    players = input("Enter the number of players: (2-4):")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("the number of players must be between 2 and 4.")
    else:
        print("Please enter a number between 2 and 4.")
max_score = 10
player_scores = [0 for _ in range(players)]
winner_found = False

while not winner_found:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll the dice? (y): ").strip().lower()
            if should_roll != 'y':
                break

            value = roll_dice()
            if value == 1:
                print("You rolled a 1! Turn over. You lose all points for this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}. Current turn score: {current_score}")

        player_scores[player_idx] += current_score
        print(f"Total score for Player {player_idx + 1}: {player_scores[player_idx]}")

        if player_scores[player_idx] >= max_score:
            print(f"\nPlayer {player_idx + 1} wins with a score of {player_scores[player_idx]}!")
            winner_found = True
            break



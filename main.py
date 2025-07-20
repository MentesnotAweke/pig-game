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

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\n Player number:", player_idx + 1 ,"turn has just starter \n")
        current_score = 0
        while True:
            should_roll = input("Do you want to roll the dice? (y): ").strip().lower()
            if should_roll != 'y':
                break
            value = roll_dice()
            if value == 1:
                print("You rolled a 1! Your turn is over, and you lose all points for this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print (f"You rolled a {value}. Your current score for this turn is {current_score}.")

        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1} total score: {player_scores[player_idx]}")

print(player_scores)
print(f"Number of players: {players}") 
 

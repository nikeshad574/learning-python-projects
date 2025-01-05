import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the Number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if players > 1 and players <= 4:
            break
        else:
            print("Number must be 2-4 players")
    else:
        print("Invalid!")


max_score = 20
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player in range(players):
        print(f"\n--------- Player {player+1} Turn ---------")
        
        tempScore = 0
        while True:
            shouldRoll = input("\nDo you want to roll the dice? (y): ")
            if(shouldRoll.lower() != "y"):
                break

            rolledNum = roll()
            if(rolledNum == 1):
                print("You Rolled 1! 0 will be added to your score.")
                tempScore = 0
                break
            else:
                print(f"You rolled {rolledNum}")
                tempScore += rolledNum
            print(f"Rolling Score: {tempScore}")

        player_scores[player] += tempScore
        print(f"Player {player+1}, Your Total Score: {player_scores[player]}")

max_score = max(player_scores)
winining_idx = player_scores.index(max_score)
print(f"Player {winining_idx+1} won the game with {max_score} score")





    
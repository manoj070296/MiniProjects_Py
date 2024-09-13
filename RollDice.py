import random

def roll_dice():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll
while True:
    no_of_players=input("Enter the number of players: ")
    if no_of_players.isdigit():
        no_of_players=int(no_of_players)
        if 2 <= no_of_players <= 4:
            break
        else:
            print("Please enter players between 2-4")
    else:
        print("Invalid Input, Pls try again")
max_score=100
player_scores=[0 for _ in range(no_of_players)]
while max(player_scores) < max_score:
    for player_idx in range(no_of_players):
        current_score = 0
        while True:
            should_roll=input("would you like to roll? ")
            if should_roll.lower() != "y":
                break
            value=roll_dice()
            if value == 1:
                print("You have rolled 1, Your turn is done")
                current_score = 0
                break
            else:
                current_score += value
                print("You have rolled a ",value)
            print("Your score is current score is ",current_score)



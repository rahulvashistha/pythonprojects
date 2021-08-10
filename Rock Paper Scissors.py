import random

player_name = input("Enter Player Name: \n")
choices = ["Rock", "Paper", "Scissors"]

print("Welcome,",player_name,"Make your choice")
player = False
cpu_score = 0
player_score = 0

while True:
    player = input("Rock, Paper or Scissors? (End to Quit)\n").capitalize()
    computer = random.choice(choices)
#Rules and Cases of the game
#Case 1
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You Win!", player, "smashes", computer)
            player_score+=1
#Case 2            
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!", computer, "cuts", player)
            cpu_score+=1
        else:
            print("You Win!", player, "covers", computer)
            player_score+=1
#Case 3
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You Win!", player, "cuts", computer)
            player_score+=1
    elif player == 'End':
#Show the final score and result
        print("Final Score")
        print(f"CPU : {cpu_score}")
        print(f"You : {player_score}")
        if player_score > cpu_score:
            print("YOU WIN!")
        elif cpu_score > player_score:
            print("YOU LOSE!")
        else:
            print("TIED!")
        break

from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = 0
while player == 0:
    player = input("Rock, Paper, Scissors,Exit?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!",'\n', computer, "covers", player)
        else:
            print("You win!",'\n', player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!",'\n', computer, "cut", player)
        else:
            print("You win!",'\n', player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...",'\n', computer, "smashes", player)
        else:
            print("You win!",'\n', player, "cut", computer)
    elif player == 'Exit':
        exit()
    else:
        print("Invalid choice.Enter valid option.")
    player = 0
    computer = t[randint(0,2)]

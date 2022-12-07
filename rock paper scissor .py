import random
t=["rock","paper","scissors"]

computer = t[random.randint(0,2)]

player = False

while player == False:
    player=input("rock,paper,scissors?")
    if player == computer:
        print("tie!")
    elif player == "rock":
        if computer == "paper":
            print("you lose!",computer,"covers",player)
        else:
            print("you win",player, "smashes",computer)
    elif player=="paper":
        if computer == "scissors":
            print("you lose")
        else:
            print("you win")
    elif player=="scissor":
        if computer == "rock":
            print("you lose")
        else:
            print("you win")
    else:
        print("that's not valid play.CHECK your spelling!")

    player=False
    computer=t[random.randint(0,2)]

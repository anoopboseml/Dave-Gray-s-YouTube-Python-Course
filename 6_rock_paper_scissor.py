# rock paper scissor game
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print(RPS(2))
print(RPS(2))
print(RPS(2))

print(" ")

player_choice = input(
    "Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

# the random.choice() method can take string, list or tuple as arg
computerchoice = random.choice([1, 2, 3])
computer = int(computerchoice)

print(" ")

print("You chose " + player_choice + ".")
print("Python chose " + str(computerchoice) + ".")
print(" ")


if player == 1 and computer == 3:
    print("✨✨✨ You win!")
elif player == 2 and computer == 1:
    print("✨✨✨ You win!")
elif player == 3 and computer == 2:
    print("✨✨✨ You win!")
elif player == computer:
    print("😢 Tie!")
else:
    print("🐍 Computer wins!")


# Dave teaches about Enum in the video but I am skipping it at this point

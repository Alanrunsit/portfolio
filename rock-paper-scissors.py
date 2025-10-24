import random

print("===================\nRock Paper Scissors\n===================")
print("\n1) ✊\n2) ✋\n3) ✌️")
player=int(input("Pick a number: "))

computer=random.randint(1,3)

symbols = {1: "✊", 2: "✋", 3: "✌️"}

print(f"\nYou chose: {symbols[player]}")
print(f"Computer chose: {symbols[computer]}")

if player == computer:
    print("It's a tie!")
elif (player == 1 and computer == 3) or \
     (player == 2 and computer == 1) or \
     (player == 3 and computer == 2):
    print("You won!")
else:
    print("Computer won!")
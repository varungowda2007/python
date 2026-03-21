import random

choices = ["rock", "paper", "scissor"]

user = input("Enter Rock, Paper or Scissor: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissor") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissor" and computer == "paper"):
    print("You Win...!")
elif user in choices:
    print("Computer Wins!")
else:
    print("Invalid input! Please enter Rock, Paper or Scissor.")
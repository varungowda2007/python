import random
choices = [ "Rock", "Paper", "Scissor"]
user = input("Enter Rock, paper, scissor : ").lower()
computer = random.choice(choices)
print("Computer Chose : ",computer)
if user == computer:
    printf("It's a Rtie!")
elif (user == "Rock" and computer == "Scissor") or \
     (user == "Paper" and computer == "Rock") or \
     (user == "Scissor" and computer == "Paper"):
    print("You Win!")
else:
     print("Computer Win!")
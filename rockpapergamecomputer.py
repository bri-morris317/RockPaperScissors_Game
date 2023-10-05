#rock paper scissors against computer player

from random import randint

#print("Welcome to the Rock, Paper, Scissors Game!")

#print("Rock...")
#print("Paper...")
#print("Scissors...")

player = input("Player 1, make your move: ").lower()

rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"

else: 
	computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
	print("Game Draw! Play again!")

elif player == "rock":
	if computer== "scissors":
		print("Player  wins!")

#	having the elif statement makes it more clear and logical. It's up to you to use elif or else:
#	elif computer == "paper":
#		print("Computer wins!")

#	having the else statement makes it more succinct	
	else:
		print("Computer wins!")

elif player == "paper":
	if computer == "rock":
		print("Player  wins!")

#	having the elif statement makes it more clear and logical. It's up to you to use elif or else:
#	elif computer == "scissors":
#		print("Computer wins!")

#	having the else statement makes it more succinct	
	else:
		print("Computer wins!")

elif player == "scissors":
	if computer == "paper":
		print("Player  wins!")
#	having the elif statement makes it more clear and logical. It's up to you to use elif or else:

#	elif computer == "rock":
#		print("Computer wins!")

	else:
		print("Computer wins!")



else:
	print("Please enter a valid move.")

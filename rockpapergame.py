#create basic version of rock, paper, scissors, game

print("Welcome to the Rock, Paper, Scissors Game!")

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

if player1 == "rock" and player2 == "scissors":
	print("Player 1 wins!")

elif player1 == "rock" and player2 == "paper":
	print("Player 2 wins!")


elif player1 == "scissors" and player2 == "paper":
	print("Player 1 wins!")

elif player1 == "scissors" and player2 == "rock":
	print("Player 2 wins!")

elif player1 == "paper" and player2 == "rock":
	print("Player 1 wins!")

elif player1 == "paper" and player2 == "scissors":
	print("Player 2 wins!")

elif player1 == player2:
	print("Game Draw! Try again!")

else:
	print("something went wrong")

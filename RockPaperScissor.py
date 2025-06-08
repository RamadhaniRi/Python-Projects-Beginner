from getpass import getpass as input

print("""
Choose one of the following options:
R = Rock
P = Paper
S = Scissors""")

player_1 = input("Player 1, make your move: ")
player_2 = input("Player 2, make your move: ")

if (player_1 == "R" and player_2 == "S") or (player_1 == "P" and player_2 == "R") or (player_1 == "S" and player_2 == "P"):
  print("Player 1 wins!")
elif (player_2 == "R" and player_1 == "S") or (player_2 == "P" and player_1 == "R") or (player_2 == "S" and player_1 == "P"):
  print("Player 2 wins!")
else:
  print("It's a tie!")
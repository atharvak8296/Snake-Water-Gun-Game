"""
SNAKE WATER GUN GAME
Snake Drinks Water : Snake Wins
Water Douses Gun : Water Wins
Gun Kills Snake : Gun Wins
"""
import random
computer = random.choice([-1, 0, 1])
print("SNAKE WATER GUN GAME")
playerStr = input("Enter s/w/g : ")
playerDict = {
  "s" : 1,
  "w" : 0,
  "g" : -1
}
player = playerDict[playerStr]
revDict = {
  1 : "Snake",
  0 : "Water",
  -1 : "Gun"
}
print(f"You have choosen {revDict[player]} whereas, Computer has choosen {revDict[computer]}")

if(player == computer):
  print("Its a Draw!")
else:
  if(player == 1):
    if(computer == 0):
      print("You Win!")
    else:
      print("You Lose!")
  if(player == 0):
    if(computer == -1):
      print("You Win!")
    else:
      print("You Lose!")
  if(player == -1):
    if(computer == 1):
      print("You Win!")
    else:
      print("You Lose!")
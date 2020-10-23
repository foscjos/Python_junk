import random
import enum

class rpsEnum(enum.Enum):
   r = 0
   p = 1
   s = 2

def Main():
  userScore = 0
  computerScore = 0
  print("Welcome to Rock, Paper, Scissors!\n")
  answer = input("Would you like to play? (Type Yes or No)\n")
  if answer.lower() == "yes":
    print("Boo Yah!")
    userScore, computerScore = playGame(userScore, computerScore)
  if answer.lower() == "no":
    print("Thanks for playing, come back soon!")
    print("You won " + str(userScore) + " games while I won " + str(computerScore) + " games. What a fun time!")
  if (answer.lower() != "yes") & (answer.lower() != "no"):
    print("Seymour Butts")

  print(userScore)
  print(computerScore)

  return;

def playGame(userScore, computerScore):
  userChoice = input("Great! Please type 'r' for 'rock', 'p' for 'paper', or 's' for 'scissors' \n")
  computerChoice = random.randint(0, 2)

  while userChoice.lower() != 'r' and userChoice.lower() != 'p' and userChoice.lower() != 's':
    userChoice = input("Oops! Please try again. r, p, or s please. \n")

  if userChoice.lower() == 'r':
    userChoice = rpsEnum.r.value
  elif userChoice.lower() == 'p':
    userChoice = rpsEnum.p.value
  else:
    userChoice = rpsEnum.s.value

  if userChoice > computerChoice:
    print("You won this round!")
    return userScore + 1, computerScore
  elif userChoice < computerChoice:
    print("I won, booh yah!")
    return userScore, computerScore + 1
  else:
    print("Draw! Nice!")
    return userScore, computerScore



Main()

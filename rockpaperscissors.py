def Main():
  print("Welcome to Rock, Paper, Scissors!\n")
  answer = input("Would you like to play? (Type Yes or No) ")
  if answer.lower() == "yes":
    print("Boo Yah!")
  if answer.lower() == "no":
    print("Eat My Shorts!")
  if (answer.lower() != "yes") & (answer.lower() != "no"):
    print("Seymour Butts")
    return;

  return;

Main()

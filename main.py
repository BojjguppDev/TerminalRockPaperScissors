import random

Options = ["rock", "paper", "scissors"]

def GetChoice(UserInput):
    choice = random.choice(Options)

    if UserInput == choice:
        result = "I chose " + choice + " Its a Tie"
        return result
    elif (UserInput, choice) in {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper")
    }:
        result = "I chose " + choice + " You Win!"
        return result
    else:
        result = "I chose " + choice + " You Lose"
        return result


UserChoice = input("Rock, Paper, or Scissors? ")

if UserChoice.lower() == Options[0]:
    GameResult = GetChoice(UserChoice)
    print(GameResult)
elif UserChoice.lower() == Options[1]:
    GameResult = GetChoice(UserChoice)
    print(GameResult)
elif UserChoice.lower() == Options[2]:
    GameResult = GetChoice(UserChoice)
    print(GameResult)
else:
    print("Not a Option")
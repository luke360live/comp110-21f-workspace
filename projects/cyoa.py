"""Life of a handyman game."""
from random import randint

__author__ = "730288863"


name = ""

points: int = 0
player: str = ""


def main() -> None:

    greet()
  
    global points
    points = 0
    i = 0
    while i < 5:
    
        decision4: str = input(f"{player} do you want to buy or fix something? (say buy or fix)")
        if decision4 == "fix":
            procedure()
        elif decision4 == "buy":
            integer()

        choice3 = input(f"Great job you now have {points} dollars, would you like to do an additional task? (say yes or no)")

        if choice3 == "yes":
            i = 0
        elif choice3 == "no":
            i = 10
        else: 
            print("That is not an option")


def greet() -> None:
    """This is the greet function."""
    global player
    player = input("what is your name? ")
    print(f"We are going to play handyman {player} the goal is to make money so you can buy things.")


def procedure() -> None:
    """This is the procedure function."""
    global points
    decision = input((f"ok {player} what do you want to fix? (you can say plumbing, fan or dishwasher)"))
    if decision == "dishwasher":
        print("")
        points = points + 10
    random_integer = randint(0, 8)
    if random_integer == 0:
        print("\U0001F329")
        print("dude, you got electrocuted working on the dishwater and had to give all your money to the hospital")
        points = 0
    else:
        print("nice job, you made 10 dollars")

    if decision == "plumbing":
        points = points + 15
        random_integer = randint(0, 10)
    if random_integer == 0:
        print("\U0001F40D")
        print("dude, you got bit buy a snake hidden and lost all your money to the hospital")
      
        points = 0
    else:
        print("nice job, you made 15 dollars")

    if decision == "fan":
        points = points + 5
        random_integer = randint(0, 1)
    if random_integer == 0:
        print("\U0001F9B4")
        print("dude, you fell from your ladder and lost all your money at the hospital, gotta work on that balance")
        points = 0
    else:
        print("nice job, you made 5 dollars")


def integer() -> int:
    """This is the integer function."""
    global points
    buychoice = input("do you want to buy a wrench or a burger (you can say wrench or burger)")
    if buychoice == "wrench" and points > 5:
        points = points - 10
        print(f"{name} that costs 10 dollars")
    elif buychoice == "burger" and points > 4:
        points = points - 3
        print(f"{name} that costs 3 dollars")
    else:
        print("this is not an option, you either spelt something wrong or do not have enough money")
  
    return points


if __name__ == "__main__":
    main()
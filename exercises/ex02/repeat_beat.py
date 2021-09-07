"""Repeating a beat in a loop."""

__author__ = "730288863"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
repeat: str = input("How many times do you want to repeat?")
i: int = 0
repea: int = int(repeat)
string: str = ""
if repea > 0:
    while i < (repea) - 1:
        string = beat + " " + string
        i = i + 1
    print(string + beat)
else:
    print("No beat...")
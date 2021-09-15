"""An exercise in remainders and boolean logic."""

__author__ = "730288863"

Given_Number: int = int(input("Enter and int: "))
if Given_Number % 14 == 0:
    print("TAR HEEELS")
else:
    if Given_Number % 2 == 0:
        print ("TAR")
    else:
        if Given_Number % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
    
"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730288863"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


fortune_one: str = "You will meet the person of your dreams soon."
fortune_two: str = "Be careful of those who are only friendly in private."
fortune_three: str = "Love is the only solution to conflict"
fortune_four: str = "Enjoy each moment and be present"
str = input("Your fortune cookie says... ")
choose: int = randint(1, 4)
if choose == 1:
    print(fortune_one)
    print("Now, go spread positive vibes!")
else:
    if choose == 2:
        print(fortune_two)
        print("Now, go spread positive vibes!")
    else:
        if choose == 3: 
            print(fortune_three)
            print("Now, go spread positive vibes!")
        else:
            print(fortune_four)
            print("Now, go spread positive vibes!")

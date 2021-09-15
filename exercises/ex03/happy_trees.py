"""Drawing forests in a loop."""

__author__ = "730288863"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth = int(input("Depth: "))
for x in range(depth):
    y = 0
    string = ""
    while y <= x:
        string = string + ("\U0001F332 ")
        y = y + 1
    print(string)
    x = x + 1

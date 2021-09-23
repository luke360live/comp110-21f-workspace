"""Drawing forests in a loop."""

__author__ = "730288863"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth = int(input("Depth: "))
i: int = 0
tree_num: str = TREE
while i < depth:
    print(tree_num)
    tree_num = tree_num + TREE
    i = i + 1
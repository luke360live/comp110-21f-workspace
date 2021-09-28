"""List utility functions."""

__author__ = "730288863"


# TODO: Implement your functions here.

"""all"""


def all(a: list[int], b: int) -> bool:
    z = 0
    while z < len(a):
        number: int = a[z]
        if b != number or a == list():
            return False
        z = z + 1
    return True 


"""is_equal"""


def is_equal(x: list[int], y: list[int]) -> bool:
    z = 0
    while z < len(x):
        list_x: int = x[z]
        list_y: int = y[z]
        if len(x) != len(y) or list_x != list_y:
            return False
        z = z + 1
    return True


"""max"""


def max(input: list) -> int:
    if input == list():
        raise ValueError
    z = 0
    biggest: int = 100
    while z < len(input):
        if input[z] > biggest:
            biggest = input[z]
        z = z + 1
    return biggest


    

    
    

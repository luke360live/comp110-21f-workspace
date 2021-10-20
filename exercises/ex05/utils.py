"""List utility functions part 2."""

<<<<<<< HEAD
__author__ = "730288863"

# Define your functions below
"""Only_evens"""


def only_evens(a: list[int]) -> list:
    evens: list[int] = []
    for x in range(len(a)):
        if a[x] % 2 == 0:
            evens.append(a[x])
        
    return evens


def sub(a: list[int], b: int, c: int) -> list:
    sublist: list[int] = []
    if b < 0:
        b = 0
    if c > len(a):
        c = len(a) - 1
       
    for x in range(b, c):
        sublist.append(a[x])
        
    return sublist


def concat(a: list[int], b: list[int]) -> list:
    list_concat: list[int] = []
    for x in range(len(a)):
        list_concat.append(a[x])
    for y in range(len(b)):
        list_concat.append(b[y])
    
    return list_concat
=======
__author__ = "123456789"

# Define your functions below
>>>>>>> b9a7730ff40ba970e5c8fa5b93bab427fcb90e6c

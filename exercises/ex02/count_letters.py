"""Counting letters in a string."""

__author__ = "730288863"


# Begin your solution here...

i: int = 0
search: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
while i < len(word): 
    how_many: str = str(word.count(search))
    print("Count: " + how_many)
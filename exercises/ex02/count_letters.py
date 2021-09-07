"""Counting letters in a string."""

__author__ = "730288863"


# Begin your solution here...

i: int = 0
search: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
count = "0"
while i < len(word):
    if word[i] == search:
        count = str(i + 1)
        break
    i = i + 1
print("Count: " + count) 
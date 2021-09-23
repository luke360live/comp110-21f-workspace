"""Finding duplicate letters in a word."""

__author__ = "730288863"

word: str = input("Enter a word: ")
length: int = len(word)
First_Letter: int = 0
Compare_Letter: int = 1
True_False: bool = False

while First_Letter < length:
    while Compare_Letter < length:
        if word[First_Letter] == word[Compare_Letter]:
            True_False = True
        Compare_Letter = Compare_Letter + 1
    First_Letter = First_Letter + 1
    Compare_Letter = First_Letter + 1
print("Found duplicate: " + str(True_False))
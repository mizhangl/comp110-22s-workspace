"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730490943"

word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if (len(character) != 1):
    print("Error: Character must be a single character.")
    exit()

counter: int = 0
print("Searching for " + character + " in " + word)

if (character == word[0]):
    counter = counter + 1
    print(character + " found at index 0")
if (character == word[1]):
    counter = counter + 1
    print(character + " found at index 1")
if (character == word[2]):
    counter = counter + 1
    print(character + " found at index 2")
if (character == word[3]):
    counter = counter + 1
    print(character + " found at index 3")
if (character == word[4]):
    counter = counter + 1
    print(character + " found at index 4")

if (counter == 0):
    print("No instances of " + character + " found in " + word)
else:
    print(str(counter) + " instances of " + character + " found in " + word)
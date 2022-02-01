"""EX02 -  A step toward's One Shot Wordle"""

__author__ = "730490943"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
while (len(guess) != len(secret)):
    guess = input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji: str = " "
while i < len(secret):
    in_letter: bool = False
    alternate: int = 0
    if guess[i] == secret[i]:
        emoji += f"{GREEN_BOX}"
    else:
        while not in_letter and alternate < len(secret): 
            if guess[i] == secret[alternate]:
                in_letter = True
                alternate += 1
            else: 
                alternate += 1      
        if in_letter:
            emoji += f"{YELLOW_BOX}"
        else: 
            emoji += f"{WHITE_BOX}"
    i += 1
print(f"{emoji}")

if guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")
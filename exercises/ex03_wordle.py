"""A step towards Wordle!"""

__author__ = "730490943"


def contains_char(word: str, char: str) -> bool:
    """Creates a function that determines if a single character is present within a given word."""
    assert len(char) == 1
    i: int = 0
    in_letter: bool = False
    while i < len(word):  # Loops through the length of a given word to check for character matches. 
        if word[i] == char:
            in_letter = True
            i += 1
        else: 
            i += 1
    if in_letter: 
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Returns emoji, specifically green, yellow, or white box codification, given two strings."""
    assert len(guess) == len(secret)
    emoji: str = ""
    counter: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8" 
    while counter < len(secret):
        if contains_char(secret, guess[counter]):  # Calls contains_char function and continues if the char at a given index in 'guess' is in the word defined by 'secret'.
            if guess[counter] == secret[counter]:  # Distinguishes if the char in 'guess' matches the corresponding letter in 'secret' both in location and letter.
                emoji += f"{GREEN_BOX}"
            else:  # If the char in 'guess' only exists in 'secret' but does not match locations, a yellow box will be concatenated. 
                emoji += f"{YELLOW_BOX}"
        else: 
            emoji += f"{WHITE_BOX}"
        counter += 1
    return emoji


def input_guess(user_input: int) -> str:
    """Given an integer's expected length of a guess as a parameter, prompt user for guess until the two match."""
    user_guess: str = input("Enter a " f"{user_input}" " character word: ")
    while (user_input) != len(user_guess):
        user_guess = input("That wasn't " f"{user_input}" " chars! Try again: ")
    return(user_guess)


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    number_played: int = 1
    won_yet: bool = True
    wordle_secret: str = "codes"
    while number_played <= (len(wordle_secret) + 1) and won_yet:  # 1 is added to len(wordle_secret) to adjust for fact that number_played begins at int = 1, rather than int = 0.
        current_turn: str = "=== Turn " + f"{number_played}" + "/" + f"{(len(wordle_secret) + 1)}" + " ==="  
        print(current_turn)
        wordle_guess = input_guess(len(wordle_secret))  # Calls function input_guess, with the parameter of length of the wordle secret word, 'codes'.
        if wordle_guess == wordle_secret:
            print(emojified(wordle_guess, wordle_secret))
            if number_played == 1:
                print(f"You won in {number_played}/{(len(wordle_secret) + 1)} turn!")
            else:
                print(f"You won in {number_played}/{(len(wordle_secret) + 1)} turns!")
            won_yet = False  # Assign while loop bool condition (won_yet) to 'False' to end the loop.
        else:
            print(emojified(wordle_guess, wordle_secret))
            number_played += 1
    if number_played > (len(wordle_secret) + 1):
        print("X/" + f"{(len(wordle_secret) + 1)}" + " - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
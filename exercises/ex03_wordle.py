"""New version of Wordle with six chances."""
__author__ = "730411607"

from mimetypes import guess_all_extensions
from re import I
import re


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(a: str, b:str) -> bool:
    """Determines if single character is in string using T/F."""
    i: int = 0
    assert len(b) == 1
    while i < len(a):
        if a[i] == b:
            return True
        else:
            i = i + 1
    if contains_char is not True:
        return False


def emojified(guess: str, secret: str) -> str:
    """Box strings are returned based on guess."""
    assert len(guess) == len(secret)
    c: int = 0
    emoji: str = ""

    while c < len(secret): 
        if guess[c] == secret[c]:
            emoji = emoji + GREEN_BOX
        else: 
            if contains_char(secret, guess[c]) is True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        c = c + 1

    return emoji 

def input_guess(expected_len: int) -> str:
    """Ensures guess is the proper length."""
    guess: str = input("Enter a " + str(expected_len) + " character word: ")

    while len (guess) != expected_len:
        guess = input("That wasn't " + str(expected_len) + " chars! Try again: ")

    return guess

def main() -> None: 
    """"This is the main control of the program loop."""
    guess: str = ""
    secret: str = "codes"
    plays: int = 1

    while plays < 7 and guess != secret:
        print(f"=== Turn {plays}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        plays += 1
    
    if plays < 7 and guess == secret:
        print(f"you won in {plays - 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main() 


    
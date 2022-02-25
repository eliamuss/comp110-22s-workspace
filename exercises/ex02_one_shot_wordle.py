"""EX02 - One Shot Wordle - A step clsoer to Wordle."""

__author__ = "730411607"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "python" 
guess: str = input(f"What is your {len(secret_word)} letter guess? ")

i: int = 0
emoji: str = ""

while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

while i < len(secret_word):
    if secret_word[i] == guess[i]:
        emoji = (emoji + GREEN_BOX)
    else:
        a: int = 0
        variable: bool = False
        while variable is not True and a < len(secret_word): 
            if secret_word[a] == guess[i]:
                variable = True 
            else:
                a = a + 1
        
        if variable is True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
            
    i = i + 1

print(emoji)

if secret_word == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
from random import choice
from tkinter import N
from colorama import Fore, Style, init
init(autoreset=True)




def game_title():
    print("Lets play wordle!")
    print("Type a five letter word and hit enter: \n")


print(Fore.RED + """

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
| ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
| |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
| |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
| |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
| |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

""")

def random_word():
    with open ("words.txt") as f:
        words = f.read().splitlines() #pulls random words from word txt file
        return choice(words)




game_title()
word = random_word()
for guess in range(1, 7): # limits the guesses to 6
    guess = input().lower()
    
    if guess == 6: 
        print("Better luck next time! You ran out of guesses")
    

    for i in range(min(len(guess), 5)): #only allows user to type no more than 5 letters
        if guess[i] == word[i]:
            print(Fore.GREEN + guess[i]) # if the letter matches the correct spot in the word it turns green
        elif guess[i] in word:
            print(Fore.YELLOW + guess[i]) # if letter is in the word then it turns yellow
        else:
            print(guess[i]) 

        if guess == word:
            print(Fore.GREEN + "Look at you! A beast at wordle! You guessed the word in " + guess[i]) # if the user guess the correct word then they win and it tells you the number of guesses
        elif guess == 6:
            print("Better luck next time! You ran out of lives")
        

                


# import nessasary files
import random
from  hangman_art import logo
from  hangman_art import stages
from  hangman_words import word_list
from replit import clear

# print some welcome msz
print("Welcome to Hangman Game")
print(logo)

# 
# lets create some words for out game
words = word_list

# now choose any word from the words
choosen_word = random.choice(words)
display = []

#  
for _ in range(len(choosen_word)):
    display += '-'

# games life
lives = len(stages) - 1

game_over = False
while not game_over:
    print(f"You have only {lives} life left")
    user_guess_letter = input("Guess a letter: ").lower()
    
    # now clear the previus input 
    clear()
    if user_guess_letter in display:
        print(f"You already type {user_guess_letter}")

    for index in range(len(choosen_word)):
        if user_guess_letter in choosen_word[index]:
            display[index] = user_guess_letter
    print(f"{' '.join(display)}")

    if user_guess_letter not in choosen_word:
        lives -= 1
        print(f"Your guess word is '{user_guess_letter}'\nThis is not correct\nYou have only {lives} life left")
    print(stages[lives])

    if lives == 0:
        print("You lose 😥")
        print(f"The result is : {choosen_word}")
        game_over = True
        

    if "-" not in display:
        game_over = True
        print("You win 😍")


    




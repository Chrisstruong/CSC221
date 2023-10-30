#  Game Hi Low Guess is a program that gives the player the opportunity to guess the number that the computer generates as a random numbe
import random

random_num = random.randint(0, 100)
continue_condition = True

def verify_guess(amount, random_num):
    your_guess = int(input("Please enter your guess: "))
    if your_guess == random_num:
        return print(f"You got it!\nIt took you {amount} guesses\n")
    if your_guess > random_num:
        print("You were high, guess again")
        verify_guess(amount + 1, random_num)
    else: 
        print("You were low, guess again")
        verify_guess(amount + 1, random_num)
        
verify_guess(1, random_num)
while continue_condition:
    print("Would you like to play again? ")
    answer = input("Enter a character ('y' for yes): ")
    if answer == 'y':
        random_num = random.randint(0, 100)
        verify_guess(1, random_num)
    else:
        continue_condition = False


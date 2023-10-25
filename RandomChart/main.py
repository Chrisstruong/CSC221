# Write a game program that prints a chart to the screen showing the randomness of a die.
import random

def print_random_chart (number_of_stars, total_throws):
    print(f"A chart of {total_throws} throws:")
    print(f"Dice number 1: {number_of_stars[0]}")
    print(f"Dice number 2: {number_of_stars[1]}")
    print(f"Dice number 3: {number_of_stars[2]}")
    print(f"Dice number 4: {number_of_stars[3]}")
    print(f"Dice number 5: {number_of_stars[4]}")
    print(f"Dice number 6: {number_of_stars[5]}")

def checking_game_condition(char):
    if char != 'y':
        return False
    else:
        return True
    
def generating_dice_num(number_of_dice_throws, chart):
    for dice in range(1, number_of_dice_throws + 1):
        random_num = random.randint(1, 6)
        if random_num == 1:
            chart[0] += '*'
        elif random_num == 2:
            chart[1] += '*'
        elif random_num == 3:
            chart[2] += '*'
        elif random_num == 4:
            chart[3] += '*'
        elif random_num == 5:
            chart[4] += '*'
        else: 
            chart[5] += '*'
    return chart

def game_condition():
    dice_chart = ['', '', '', '', '', '']
    number_of_dice_throws = int(input("Please enter positive number of dice throws you want. "))
    # Checking if num of dice throws is negative
    while number_of_dice_throws <= 0:
        number_of_dice_throws = int(input("Please enter positive number of dice throws you want. "))
    # Generating * for each index in dice_chart
    dice_chart = generating_dice_num(number_of_dice_throws, dice_chart)
    # Print out the chart
    print_random_chart(dice_chart, number_of_dice_throws)
    # Asking if the client would like to run again
    print("Would you like to play again?")
    char_response = input("Enter a character ('y' for yes): ")
    print()
    if char_response == 'y':
        game_condition()

game_condition()

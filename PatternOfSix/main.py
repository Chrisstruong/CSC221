# Write a game program that prompts for a pattern of 6 dice and then counts the number of throw necessary to get that pattern to appea
import random

def continue_condition(answer):
    if answer == "yes":
        print()
        compare_input_and_random_num(0)
    else:
        print("Goodbye!")

def generating_random_num():
     return (str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))

def compare_input_and_random_num(counting_iteration):
    list_of_six_numbers = 0
    six_number_pattern_input = input("Please enter the six_number pattern you would like the computer to throw seperated spaces: ")
    six_number_pattern = six_number_pattern_input.replace(" ", "")
    while list_of_six_numbers != six_number_pattern:
        list_of_six_numbers = generating_random_num()
        # print(list_of_six_numbers)
        counting_iteration += 6
    print(f"It took {counting_iteration:,} throws to get the pattern {six_number_pattern_input}")
    continue_condition(input("Would you like to play the game again(yes/no)? "))

compare_input_and_random_num(0)

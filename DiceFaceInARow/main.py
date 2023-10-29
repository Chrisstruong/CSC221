# This game throws a dice until a particular dice face number appears in a row a certain number of times.
import random

# Function for option 1
def trace_the_game(target_times_repeated_in_a_row, target_num):
    number_of_throws = 1
    times_repeated_in_a_row_in_function = 0
    while times_repeated_in_a_row_in_function != target_times_repeated_in_a_row:
        random_num = random.randint(1, 6)
        if random_num == target_num:
            times_repeated_in_a_row_in_function += 1
        else: 
            times_repeated_in_a_row_in_function = 0
        print(f"You got a {random_num}")
        print(f"Number of times in a row so far is {times_repeated_in_a_row_in_function}")
        print(f"Number of throws is {number_of_throws:,}")
        number_of_throws += 1

# Function for option 2
def immediate_answer(target_times_repeated_in_a_row, target_num):
    number_of_throws = 1
    times_repeated_in_a_row_in_function = 0
    while times_repeated_in_a_row_in_function != target_times_repeated_in_a_row:
        random_num = random.randint(1, 6)
        if random_num == target_num:
            times_repeated_in_a_row_in_function += 1
        else:
            times_repeated_in_a_row_in_function = 0
        number_of_throws += 1
    print(f"It took {(number_of_throws - 1):,} throws to get the number {target_num} to appear {target_times_repeated_in_a_row} in a row")    

# Main function
def main_function():
    print("Please enter the version you want: ")
    print("\t1) Trace the game.")
    print("\t2) Just give the answer.")
    version = input("Please enter 1 or 2: ")
    target_num = int(input("Please enter the dice face number that you would like to be repeated. "))
    target_times_repeated_in_a_row = int(input(f"Please enter the number of times that you would like {target_num} to appear in a row. "))
    if version == "1":
        trace_the_game(target_times_repeated_in_a_row, target_num)
    else: 
        immediate_answer(target_times_repeated_in_a_row, target_num)
    continue_or_not = input("Would you like to play the game again (yes/no)? ")
    if continue_or_not == 'yes':
        print()
        main_function()
    else: 
        print("Goodbye!")

main_function()

   



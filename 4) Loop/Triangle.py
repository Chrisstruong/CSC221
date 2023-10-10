# 1) Write a program that draws a triangle. Terminate when user enters 'q'

# Read the input
user_input = input("Enter number of lines wanted: ")

while user_input != 'q':
    # convert data type
    user_input = int(user_input)
    # print * for first half of triangle
    for increase in range(1, user_input + 1):
        print('\033[1;36;40m*\033[0m' * increase)
    # print * for second half of triangle
    for decrease in range(user_input - 1, 0, -1):
        print('\033[1;36;40m*\033[0m' * decrease)
    # read user input again
    user_input = input("Enter number of lines wanted (q to terminate): ")
print("Merci!")
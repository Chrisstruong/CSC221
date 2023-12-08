# 1) Write a program that reads two numbers. The first is positive and the second is negative. Multiply them together and print the product. Keep reading pairs as long as the first is positive and the second is negative.

# num1 = 1
# num2 = -1

# while num1 > 0 and num2 < 0:
#     num1 = int(input("Please enter your first number: "))
#     num2 = int(input("Please enter your second number: "))
#     print(f"Product of two numbers are: {num1 * num2}")
#     print()

# print("The program terminates because one of the condition failed")

# 2) Write a program that reads three numbers. Their sum must be positive. Add them together as long as their sum is positive and print the sum. Keep reading sets of three numbers as long as the sum is positive.

# num1 = 1
# num2 = 2
# num3 = 3
# sum_of_three_num = 1
# while sum_of_three_num > 0:
#     num1 = int(input("Please enter your first num: "))
#     num2 = int(input("Please enter your second num: "))
#     num3 = int(input("Please enter your third num: "))
#     sum_of_three_num = num1 + num2 + num3
#     if (sum_of_three_num > 0):
#         print(f"The sum of three numbers are {sum_of_three_num}")
#         print("You may continue")
#     else:
#         print("Your sum is < 0 => You are done")



# 3) Write the code segment that uses a loop to sum the integers starting with the integer 1 and stopping when the sum of the integers is greater than 10,000. When the loop finishes print the number that was the last integers added to the sum to put the sum over 10,000
# starting_num = 1
# number_sum = 0
# while number_sum <= 10000:
#     number_sum += starting_num
#     starting_num += 1
# print(f"The number that put sum over 10,000 is {starting_num}")


# 4) Write the code segment that uses a loop to read 10 integers numbers. Add the even numbers and add the odd numbers. Print these two sums at the end.

# sum_of_even_nums = 0
# sum_of_odd_nums = 0
# for round in range(11):
#     num = int(input("Please enter a number: "))
#     if num % 2 == 0:
#         sum_of_even_nums += num
#     else:
#         sum_of_odd_nums += num

# print(f"Sum of even nums is {sum_of_even_nums}")
# print(f"Sum of odd nums is {sum_of_odd_nums}")

# 5) Write the code segment that uses a loop to create the cubes of the frist 15 even numbers.
# number = 2 
# counter = 1
# while counter <= 15:
#     cubic = number ** 3
#     print(f"The cubic of number {number} is {cubic}")
#     number += 2
#     counter += 1

# 6) Write the code segment that uses a loop to read a number called test_value. Read 10 more numbers and compare them to test_value. Print if the number is less than test_value, greater than test_value or the same
# test_value = int(input("Enter your test value: "))
# counter = 1
# while counter <= 10:
#     print(f"Round {counter}")
#     test_number = int(input("Enter your test number: "))
#     if test_number > test_value:
#         print(f"Test number {test_number} is greater than test value {test_value}")
#     elif test_number == test_value:
#         print(f"Test number {test_number} is equavilient to test value {test_value}")
#     else:
#          print(f"Test number {test_number} is smaller to test value {test_value}")
#     counter += 1

# 7) Write the code segment that uses a loop to read 15 numbers. Print the largest number, the smallest number and the average of the 15 numbers.
# test_number = int(input("Please enter a number: "))
# max_num = test_number
# min_num = test_number
# sum = test_number
# counter = 1

# while counter <= 14:
#     test_number = int(input("Please enter a number"))
#     if (max_num < test_number):
#         max_num = test_number
#     if (min_num > test_number):
#         min_num = test_number
#     sum += test_number
#     counter += 1

# print(f"The largest number is {max_num}")
# print(f"The smallest number is {min_num}")
# print(f"The average of 15 numbers is {sum / 15}")

# 8) Write the code segment that uses a loop to read 15 positive integer numbers. Print the largest number of the 15 numbers

# max_num = -1
# counter = 1

# while counter <= 15:
#     test_number = int(input(f"Enter a number in round {counter}: "))
#     if max_num < test_number:
#         max_num = test_number
#     counter += 1

# print(f"The largest num is {max_num}")

# 9) Write the code segment that uses a loop to print the first 50 even integers numbers.
# test_number = 0
# while test_number <= 50:
#     print(f"The value is: {test_number}")
#     test_number += 2

# 10) Using a loop, write a program that reads 10 numbers and calculates the average of the numbers and prints this average at the end of the program
# sum_of_nums = 0
# for num in range(1, 11):
#     print(num)
#     test_value = int(input("Please enter a value: "))
#     sum_of_nums += test_value

# print(f"The average is {sum_of_nums / 10}")

# 11) Write a program that reads values for number1, number2, number3 and displays their sum, repeating the input as long as none of the three values are negative.

# number1 = int(input("Please enter a first number: "))
# number2 = int(input("Please enter a second number: "))
# number3 = int(input("Please enter a third number: "))
# sum_of_nums = number1 + number2 + number3
# print(f"Sum of three numbers is {sum_of_nums}")

# while number1 >= 0 and number2 >= 0 and number3 >= 0:
#     number1 = int(input("Please enter a first number: "))
#     number2 = int(input("Please enter a second number: "))
#     number3 = int(input("Please enter a third number: "))
#     sum_of_nums = number1 + number2 + number3
#     print(f"Sum of three nums is {sum_of_nums}")

# print(f"It's over! One of your nums is negative.")

# 12) Please enter a series of positive integer number. Print the sum of the series as it is created. A negative number of zero will end the series.
# num = int(input("Please enter a number "))
# sum_of_nums = 0

# while num > 0:
#     sum_of_nums += num
#     print(f"The sum of numbers is {sum_of_nums}")
#     num = int(input("Please enter a number "))

# print(f"The number you just entered {num} is negative or zero")
# 1) Write a program that reads two numbers. The first is positive and the second is negative. Multiply them together and print the product. Keep reading pairs as long as the first is positive and the second is negative.

# number1 = 1
# number2 = -1
# while number1 > 0 and number2 < 0:
#     number1 = int(input("Please enter a positive number: "))
#     number2 = int(input("Please enter a negative number: "))
#     product = number1 * number2
#     print(f"The product of two numbers are {product}")

# print("The first num is no longer positve and the second negative")

# 2) Write a program that reads three numbers. Their sum must be positive. Add them together as long as their sum is positive and print the sum. Keep reading sets of three numbers as long as the sum is positive.
# sum_of_nums = 1
# while sum_of_nums > 0:
#     number1 = int(input("Please enter the first num"))
#     number2 = int(input("Please enter the second num"))
#     number3 = int(input("Please enter the third num"))
#     sum_of_nums = number1 + number2 + number3
#     print(f"The sum of sets of three numbers is {sum_of_nums}")

# print("The sum is no longer positive")

# 3) Write the code segment that uses a loop to sum the integers that starting with the integer 1 and stopping when the sum of the integers is greater than 10,000. When the loop finishes print the number that was the last integer added to the sum to put the sum over 10,000.

# sum_of_numbers = 0
# counter = 1
# while sum_of_numbers <= 10000:
#     sum_of_numbers += counter
#     counter += 1

# print(f"The last integer is {counter, sum_of_numbers}")

# 4)Write the code segment that uses a loop to read 10 integer numbers. Add the even numbers and add the odd numbers. Print these two sums at the end.

# sum_of_even_nums = 0
# sum_of_odd_nums = 0
# for num in range(10):
#     reading_num = int(input("Please an integer number: "))
#     if reading_num % 2 == 0:
#         sum_of_even_nums += reading_num
#     else:
#         sum_of_odd_nums += reading_num

# print(f"Sum of even numbers is {sum_of_even_nums}")
# print(f"Sum of odd numbers is {sum_of_odd_nums}")
    

# 5) Write the code segment that uses a loop to create the cubes of the first 15 even numbers
# counter = 1
# num = 2
# while counter <= 15:  
#     cube = num ** 3
#     print(f"{num} cubed is {cube}")
#     num += 2
#     counter += 1

# 6) Write the code segment that uses a loop to read a number called test_value. read 10 more numbers and compare them to test_value. Print if the number is less than test_value, greater than test_value or the same

# test_value = int(input("Enter a test value: "))
# for num in range(10):
#     test_num = int(input("Enter a test number: "))
#     if (test_value > test_num):
#         print(f"Test value {test_value} is greater than test num")
#     elif(test_value == test_num):
#         print(f"Test value {test_value} is the same as {test_num}")
#     else:
#         print(f"The test value {test_value} is smaller than test num {test_num}")

# 7) Write the code segment that uses a loop to read 15 numbers. Print the largest number, the smaller number, and the average of the 15 numbers.
# number = int(input("Please enter a number in round 1: "))
# largest_num = number
# smallest_num = number
# sum_of_nums = number
# counter = 2
# while counter <= 15:
#     number = int(input(f"Please enter a number in round {counter}: "))
#     if (largest_num < number):
#         largest_num = number
#     if smallest_num > number:
#         smallest_num = number
#     sum_of_nums += number
#     counter += 1

# print(f"The largest number is {largest_num}")
# print(f"The smallest number is {smallest_num}")
# print(f"The average of 15 numbers is {sum_of_nums / 15:.2f}")

# 8) Write the code segment that uses a loop to read 15 positive integers numbers. Print the largest number of 15 numbers.
# number = int(input("Please enter number in round 1: "))
# largest_number = number

# for round in range(2, 16):
#     number = int(input(f"Please enter number in round {round}: "))
#     if (largest_number < number):
#         largest_number = number

# print(f"The largest number is {largest_number}")   

# 9) Write the code segment that uses a loop to print the first 50 even integer numbers
# even_number = 2
# for round in range(1, 51):
#     print(f"The even number in round {round} is {even_number}")
#     even_number += 2

# 10) Using a loop, write a program that reads 10 numbers and calculates the averages of the numbers and prints this average at the end of programs.

# sum = 0
# for round in range(1, 11):
#     number = int(input(f"Please enter number in round {round}: "))
#     sum += number

# print(f"The average of 10 numbers is {sum / 10:.2f}")

# 11) Write a program that reads values for number 1, number2, number3 and displays their sum, repeating the input as long as none of the three values are negative.

# number1, number2, number3 = 1, 1, 1
# sum_of_nums = 0
# while number1 >= 0 and number2 >= 0 and number3 >= 0:
#     number1 = int(input("Please enter value for number 1: "))
#     number2 = int(input("Please enter value for number 2: "))
#     number3 = int(input("Please enter value for number 3: "))
#     if number1 >= 0 and number2 >= 0 and number3 >= 0:
#         sum_of_nums = number1 + number2 + number3
#         print(f"Sum of three numbers is {sum_of_nums}")

# print("One of your numbers was negative")

# 12) Please enter a series of positive integer number. Print the sum of the series as it is created. A negative number or zero will end the series.

positive_number = int(input("Please enter a positive number: "))
sum_of_the_nums = 0
while positive_number > 0:
    sum_of_the_nums += positive_number
    print(f"The sum of a series of positive number is {sum_of_the_nums}")
    positive_number = int(input("Please enter a positive number: "))

print("A negative or zero number just entered.")





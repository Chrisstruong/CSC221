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

sum_of_even_nums = 0
sum_of_odd_nums = 0
for round in range(11):
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        sum_of_even_nums += num
    else:
        sum_of_odd_nums += num

print(f"Sum of even nums is {sum_of_even_nums}")
print(f"Sum of odd nums is {sum_of_odd_nums}")
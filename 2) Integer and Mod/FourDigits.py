# 1) Write a program that reads a 4-digit integer, and then displays it one digit per line.

# Solution:
# 1) Display a prompt reads a 4-digit integer
four_digit_number = int(input("Enter 4-digt integer: "))

# 2) Find first digit (thousands)
first = four_digit_number // 1000
# 3) Find second digit (hundreds)
second = four_digit_number // 100 % 10
# 4) Find third digit (tens)
third = four_digit_number // 10 % 100 % 10

# 5) Find last digit (ones)
last = four_digit_number % 1000 % 100 % 10

# 6) Display each digit place
print(first)
print(second)
print(third)
print(last)

# 3) Write a program that reads a four-bit binary number and then converts it into decimal

# Solution:
# 1) Display a prompt
four_bit_num = int(input("Enter a four-bit binary number: "))

# 2) Find the thousands
first_num = four_bit_num // 1000
# 3) Find the hundreds
second_num = four_bit_num // 100 % 10
# 4) Find the tens
third_num = four_bit_num // 10 % 100 % 10
# 5) Find the ones
last_num = four_bit_num % 1000 % 100 % 10

# 6) Binary to decimal fomula
binary_to_decimal = (8 * first_num) + (4 * second_num) + (2 * third_num) + (last_num)

# 7) Display the decimal
print(f"If the number is {four_bit_num}, the answer is {binary_to_decimal}")
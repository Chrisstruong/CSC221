four_bit_num = int(input("Enter a four-bit binary number: "))

first_num = four_bit_num // 1000
second_num = four_bit_num // 100 % 10
third_num = four_bit_num // 10 % 100 % 10
last_num = four_bit_num % 1000 % 100 % 10

binary_to_decimal = 8 * first_num + 4 * second_num + 2 * third_num + last_num

print(first_num)
print(second_num)
print(third_num)
print(last_num)

print(binary_to_decimal)
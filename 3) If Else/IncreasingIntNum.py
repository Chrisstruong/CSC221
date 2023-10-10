# 2) Write a program to read three positive integers from the keyboard and display them each on their own line in increasing order.
num = input("Enter 3 positive integers: ")
first_num = num[0]
second_num = num[1]
third_num = num[2]


# Solutions:
# 1) Get the last num
if (num[0] > num[2]) and (num[0] > num[1]):
    third_num = num[0]
    
elif (num[1] > num[0]) and (num[1] > num[2]):
    third_num = num[1]
else:
    third_num = num[2]


# 2) Get the first num
if (num[0] < num[2]) and (num[0] < num[1]):
    first_num = num[0]
elif (num[1] < num[0]) and (num[1] < num[2]):
    first_num = num[1]
else: 
    first_num = num[2]

num = num.replace(first_num, '')
num = num.replace(third_num, '')

# 3) Get the second num
second_num = num
print(first_num)
print(second_num)
print(third_num)
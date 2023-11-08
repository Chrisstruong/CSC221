import random, math
# size_list = int(input("How large is your list? "))
size_list = 8
num_list = [2, 4, 4, 4, 5, 5, 7, 9]

# for num in range(size_list):
#     random_num = random.randint(0, 100)
#     num_list.append(random_num)

print(num_list)
max = max(num_list)
min = min(num_list)
sum = sum(num_list)
average_num_list = sum / size_list
print(average_num_list)

deviation_list = []
for num in num_list:
    mean_data_point = (num - average_num_list) ** 2
    deviation_list.append(mean_data_point)

print(deviation_list)
def calculate_deviation_sum(list, sum):
    for num in list:
        sum += num
    return sum

sum_deviation = calculate_deviation_sum(deviation_list, 0)
average_deviation_list = sum_deviation / size_list
standard_deviation = math.sqrt(average_deviation_list)
print(f"Standard Deviation is: {standard_deviation}")
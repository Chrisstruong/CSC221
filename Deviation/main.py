import random, math

def size_input():
    size_list = int(input("How large is your list? "))
    random_num_list = generating_random_num(size_list)
    max = find_max(random_num_list)
    min = find_min(random_num_list)
    sum = find_sum(random_num_list)
    average = find_average(sum, size_list)
    deviation_list = generating_deviation_list(random_num_list, average)
    deviation_value = calculate_deviation_value(deviation_list, size_list)
    print_out(random_num_list, max, min, sum, average, deviation_value) 
    continue_condition = input("Do you want to do another List? (enter y for yes) ")
    if continue_condition == 'y':
        size_input()
    else:
        print("Goodbye!")

def generating_random_num(size):
    num_list = []
    for num in range(size):
        random_num = random.randint(0, 100)
        num_list.append(random_num)
    return num_list

def generating_deviation_list(num_list, average):
    deviation_list = []
    for num in num_list:
        mean_data_point = (num - average) ** 2
        deviation_list.append(mean_data_point)
    return deviation_list

def calculate_deviation_value(dev_list, size):
    sum_dev = find_sum(dev_list)
    dev_value = math.sqrt(sum_dev / size)
    return dev_value

def print_out(num_list, max, min, sum, average, dev_value):
    print(num_list)
    print(f"The maximum number in the list is {max}")
    print(f"The minimum number in the list is {min}")
    print(f"The array_sum is {sum}")
    print(f"The average is {average}")
    print(f"standard_deviation is {dev_value}")
    print()
    
def find_max(num_list):
    return max(num_list)

def find_min(num_list):
    return min(num_list)

def find_sum(num_list):
    return sum(num_list)

def find_average(sum, size):
    return sum / size


size_input()

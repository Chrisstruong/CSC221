import random
def input_data():
    list_size = int(input("Give me the sign of the list: "))
    list_values = [0] * list_size
    for index in range(list_size):
        list_values[index] = random.randint(1, 6)
    return list_values

def process(list_values):
    list_size = len(list_values)
    sum_values = 0
    for index in range(list_size):
        list_values[index] *= 100
        sum_values += list_values[index]
    print(f"The sum of the values is {sum_values}")
    
def output(list_values):
    print(f"The values of list are {list_values}")

generated_list_values = input_data()
process(generated_list_values)
output(generated_list_values)

# import random
# def inputData():
#     print('This is like a final exam question. It has three functions.')
#     print('They are input, process, and output. The input function')
#     print('is giving you this information and asking for some input.')
#     print('The random number function is used.')
#     print('What is the size of the list you want?')
#     listSize = int(input())
#     listValues = [0] * listSize
#     count = 0
#     while count < listSize:
#         listValues[count] = random.randint(1,6)
#         count += 1
#     return listValues 

# def process(listValues):
#     print(listValues)
#     counter = 0
#     listSize = len(listValues)
#     while counter < listSize:
#         listValues[counter] = listValues[counter] * 100
#         counter += 1
#     addingValues = 0
#     counter = 0
#     while counter < listSize:
#         addingValues = addingValues + listValues[counter]
#         counter += 1
#     print('the sum of listValues is',addingValues)
#     return listValues

# def answer(listValues):
#     print('The values in listValues are')
#     print(listValues)

# listValues = inputData()
# theListValues = process(listValues)
# answer(listValues)

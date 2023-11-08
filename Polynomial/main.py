def enter_degree():
    degree = int(input("Please enter the degree of the polynomial you would like. "))
    polynomial = adding_coefficient(degree)
    print(polynomial)
    x_value = int(input("What value of x would you like to use evaluate the polynomial? "))
    index = 0
    sum_calculation(0, 0, x_value, polynomial)
    continue_answer = input("Do you want to evaluate another Polynomial? (enter y for yes) ")
    if continue_answer == 'y':
        enter_degree()
    else:
        return -1
def adding_coefficient(degree):
    coef_list = []
    for num in range(degree + 1):
        coefficient = int(input(f"please enter your coefficient for degree {num} "))
        coef_list.append(coefficient)
    return coef_list
def sum_calculation(index, sum, x, equation):
    for value in equation:
        sum += value * (x ** index)
        index += 1
    output_sum(sum)
def output_sum(sum):
    print(f"sumOfTerms is {sum}")


enter_degree()

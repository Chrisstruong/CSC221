
def get_numbers():
    values = []
    for count in range(6):
        values.append(int(input()))
    return values

def print_selected_numbers():
    numbers = get_numbers()
    for number in numbers:
        if number > 2:
            print(number)

print_selected_numbers()
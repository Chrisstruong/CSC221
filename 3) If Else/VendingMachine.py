# 1) Write a program that determines the change to be dispensed from a vending machine.

# Solutions:
# 1) Read item price
item_price = int(input("Enter price of new item (in cents): "))

# 1st condition when item_price > 100
if item_price > 100:
    print("The input is more than a dollar.")
# 2nd condition when item_price < 25
elif item_price < 25:
    print("The input is less than 25 cents.")
# 3rd condition when item_price % 5
elif item_price % 5 != 0:
    print("the input is not divisible by 5.")
else:
    change = 100 - item_price
    quarters = change // 25 # Expression to get quarters
    change %= 25
    dimes = change // 10 # Expression to get dimes
    change %= 10
    nickels = change // 5 # Expression to get nickels
    print(f"You bought an item for {item_price} cents and gave me a dollar, so your change is")
    print(f"{quarters} quarters,")
    print(f"{dimes} dimes, and ")
    print(f"{nickels} nickels")
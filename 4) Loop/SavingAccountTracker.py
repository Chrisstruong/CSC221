# 3) Write a program for computing the month-by-month balance in your savings account. 
saving_balance = int(input("Enter your saving acccount balance: "))
print("_______________________")
# interest rate constant
interest_rate = 0.05

# to track whether deposit or withdrawal
transaction = 0
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for month in month_list:
    print(f"\033[1;36;40m{month}\033[0m: Your current balance is \033[1;36;40m${saving_balance:,.2f}\033[0m")
    # checking if the user deposit or withdraw
    deposit_or_withdrawal = input(f"Would you like to deposit or withdrawal in {month} (d or w): ")
    if deposit_or_withdrawal == 'd':
        transaction = int(input(f"How much do you want to deposit? "))
        saving_balance += transaction
    else:
        transaction = int(input(f"How much do you want to withdrawal? "))
        saving_balance -= transaction
    # Calculation for saving balance after deposit or withdrawal
    saving_balance +=  (saving_balance * interest_rate)
    print("_______________________")
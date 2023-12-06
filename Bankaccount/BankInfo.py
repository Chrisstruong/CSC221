# Main class
class BankInformation:
    def __init__(self, name):
        self.name = name
        self.start_balance = float(input(f"{self.name}, enter your starting balance: "))
    def deposit(self):
        deposit_amount = float(input(f"{self.name}, how much were you paid this week? "))
        self.start_balance += deposit_amount
    def withdraw(self):
        withdraw_amount = float(input(f"{self.name}, how much would you like to withdraw? "))
        self.start_balance -= withdraw_amount
    def get_balance(self):
        print(f"{self.name}, your account balance is ${self.start_balance:,.2f}")


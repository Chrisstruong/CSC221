# Inherit class
from BankInfo import BankInformation

Sue = BankInformation("Sue")
Tom = BankInformation("Tom")
Bob = BankInformation("Bob")
print()

bank_information_list = [Tom, Sue, Bob]
for info in bank_information_list:
    info.deposit()
    info.get_balance()
    info.withdraw()
    info.get_balance()
    print()
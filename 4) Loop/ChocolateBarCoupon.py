# 4) Write a program to calculate additional chocolate bars
chocolate_expense = int(input("How much money would you like to buy chocolate? "))
coupon = chocolate_expense

total_chocolate = chocolate_expense + (coupon // 6)
coupon = coupon // 6 + coupon % 6 # Calculate coupon after redeming each time

while coupon >= 6:
    total_chocolate += coupon // 6 
    coupon = coupon // 6 + coupon % 6



print(f"For {chocolate_expense} dollars, we could have consumed {total_chocolate} chocolate bars and still have {coupon} coupon(s) left")


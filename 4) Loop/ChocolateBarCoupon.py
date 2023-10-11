print(5 // 6)
chocolate_expense = int(input("How much money would you like to buy chocolate? "))
coupon = chocolate_expense

total_chocolate = chocolate_expense + (coupon // 6)
print(total_chocolate)
coupon_remainder = total_chocolate % 6
if coupon_remainder == 0:
    total_chocolate += 1
    coupon_remainder = total_chocolate % 6




print(f"For {chocolate_expense} dollars, we could have consumed {total_chocolate} chocolate bars and still have {coupon_remainder} coupon(s) left")


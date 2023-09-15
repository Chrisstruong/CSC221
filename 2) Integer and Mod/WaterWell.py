# 5) Write a program that allows the user to input the radius of the well casing in inches and the depth of the well in feet. The program should output the number of gallons stored in the casing.

import math

# 1) Display a prompt for the radius of the well
well_radius = int(input("Enter a radius of the well (in inches): "))

# 2) Display a prompt for the depth of the well
well_depth = int(input("Enter a depth of the well (in feet): "))
print()

#  3) Convert radius in inches to feet. Then do volume of the cylinder: V = pi * r^2 * h
#  1 foot = 12 inch
volume = math.pi * ((well_radius / 12) ** 2) * well_depth

# 4) 1 cubic foot = 7.48 gallons: water amount = 7.48 * volume
water_amount = round(volume * 7.48)

# 5) Output the number of gallons stored in the casing.
if water_amount >= 250:
    print(f"A {well_depth}-foot well full of water with a radius of {well_radius} inches for the casing holds about {water_amount} gallons of water - plenty for a family of four and no need to install a seperate holding tank.")
else:
    print(f"A {well_depth}-foot well full of water with a radius of {well_radius} inches for the casing holds about {water_amount} gallons of water - not enough for a family of four and need to install a seperate holding tank")




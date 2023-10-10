# 4) The body mass index (BMI) is used to estimate the risk of weight-related problems based on a subject’s height and mass.
height_in_feet = float(input("Enter your height in feet: "))
height_in_inch = float(input("Enter your height in inch: "))
mass_in_pound = int(input("Enter your mass in pounds: "))

# Convert height to all inches
total_height_in_inch = height_in_feet * 12 + height_in_inch

# Convert mass from pound to kg
mass_in_kg = mass_in_pound / 2.2
# Convert height in inches to meters
total_height_in_meter = total_height_in_inch * 0.0254

# Calculate BMI index
bmi = mass_in_kg / (total_height_in_meter * total_height_in_meter)

print(f"After conversion, your weight is {mass_in_kg:.2f}kg and height is {total_height_in_meter:.2f}m")
input("")

# Main output
if bmi >= 30:
    print(f"Your bmi is \033[1;36;40m{bmi:.1f}\033[0m, indicating your weight is in the \033[1;36;40mObese\033[0m category")
elif bmi >= 25 and bmi < 30:
    print(f"Your bmi is \033[1;36;40m{bmi:.1f}\033[0m, indicating your weight is in the \033[1;36;40mOverweight\033[0m category")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi is \033[1;36;40m{bmi:.1f}\033[0m, indicating your weight is in the \033[1;36;40mNormal Weight\033[0m category")
else:
    print(f"Your bmi is \033[1;36;40m{bmi:.1f}\033[0m, indicating your weight is in the \033[1;36;40mUnderweight\033[0m category")


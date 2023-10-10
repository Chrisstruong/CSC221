# 3) Write a program that allows the user to convert a temperature give in degrees from either Celsius to Fahrenheit or from Fahrenheit to Celsius
degrees_type = input("What kind of temp you would like to convert (C or F)? ")
degrees = int(input("What's your current degrees? "))

degrees_type = degrees_type.upper()
converted_degrees = degrees
converted_degrees_type = degrees_type
if degrees_type == "C":
    converted_degrees = (9.0 * (degrees) / 5.0) + 32
    degrees_type = "Celsius"
    converted_degrees_type = "Fahrenheit"
else:
    converted_degrees = 5.0 * (degrees - 32) / 9.0
    converted_degrees_type = "Celsius"
    degrees_type = "Fahrenheit"

converted_degrees = round(converted_degrees, 2)

print(f"Your input is {degrees} degrees {degrees_type}. We are going to convert to {converted_degrees_type} degrees")
input("")

# Main output
print(f"{degrees} degrees {degrees_type} is \033[1;36;40m{converted_degrees}\033[0m degrees {converted_degrees_type}")



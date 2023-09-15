# 4) Write a program that converts degrees from Fahrenheit to Celsius.

# 1) Display a prompt for degrees f
degrees_f = int(input("Enter a temperature in degrees Fahrenheit: "))

# 2) Using the formula: Conversion DegreesC = 5(DegreesF -32)/9
conversion_degrees_c = round(5 * (degrees_f - 32) / 9, 2)

# 3) Output the degrees C
print(f"{degrees_f} degrees Fahrenheit is {conversion_degrees_c} degrees Celsius.")

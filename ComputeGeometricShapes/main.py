# There are five circle or sphere values that this program calculates. The client
# chooses one of the values and the program calculates the other four values.
# Which circle or sphere calculation would you like to start with?
# 1) Radius
# 2) Circle Circumference
# 3) Circle Area
# 4) Sphere Area
# 5) Sphere Volume

import math
import os

def continue_condition():
    print("Would you like to play the game again?")
    answer = input("Please enter (yes/no) ")
    if answer == "yes":
        os.system('cls||clear')
        output_instruction()
    else: 
        return print("Goodbye!")

def output(radius, circle_circum, circle_area, sphere_area, sphere_volume):
    print(f"The radius of the circle is {radius}")
    print(f"The circumference of the circle is {circle_circum}")
    print(f"The area of the circle is {circle_area}")
    print(f"The area of the sphere is {sphere_area}")
    print(f"The volume of the sphere is {sphere_volume}")

def output_instruction():
    print("Which circle or sphere calculation would you like to start with?")
    print("1) Radius")
    print("2) Circle Circumference")
    print("3) Circle Area")
    print("4) Sphere Area")
    print("5) Sphere volume")
    option = int(input())
    if option == 1:
        given_radius()
    elif option == 2:
        given_circle_circum()
    elif option == 3:
        given_circle_area()
    elif option == 4:
        given_sphere_area()
    else:
        given_sphere_volume()

def given_radius():
    radius = float(input("Please enter the radius: "))
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * (radius ** 2)
    sphere_area = 4 * math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    output(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()

def given_circle_circum():
    circle_circumference = float(input("Please enter your circle circunference: "))
    radius = circle_circumference / (2 * math.pi)
    circle_area = math.pi * (radius ** 2)
    sphere_area = 4 * math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    output(radius, circle_circumference, circle_area, sphere_area, sphere_volume)   
    continue_condition()

def given_circle_area():
    circle_area = float(input("Please enter your circle area: "))
    radius = math.sqrt(circle_area / math.pi)
    circle_circumference = 2 * math.pi * radius
    sphere_area = 4 * math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    output(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()


def given_sphere_area():
    sphere_area = float(input("Please enter your sphere area: "))
    radius = math.sqrt(sphere_area / (4 * math.pi))
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    output(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()

def given_sphere_volume():
    sphere_volume = float(input("Please enter your sphere volume: "))
    radius = ((3 * sphere_volume) / (4 * math.pi)) ** (1/3)
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * (radius ** 2)
    sphere_area = 4 * math.pi * (radius ** 2)
    output(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()

output_instruction()
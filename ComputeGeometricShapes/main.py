# There are five circle or sphere values that this program calculates. The client chooses one of the values and the program calculates the other four values.
# Which circle or sphere calculation would you like to start with?
# 1) Radius
# 2) Circle Circumference
# 3) Circle Area
# 4) Sphere Area
# 5) Sphere Volume

import math
import os

def introduction_CircleAndSphere():
    print("There are five circle or sphere values that this program calculates. The client chooses one of the values and the program calculates the other four values.")

def startWithRadius():
    radius = float(input("Please enter the radius: "))
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * (radius ** 2)
    sphere_area = 4 * math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    printCalculations(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()

def startWithCircumference():
    circle_circumference = float(input("Please enter your circle circunference: "))
    radius = circle_circumference / (2 * math.pi)
    circle_area = math.pi * (radius ** 2)
    sphere_area = 4 * math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    printCalculations(radius, circle_circumference, circle_area, sphere_area, sphere_volume)   
    continue_condition()

def startWithCircleArea():
    circle_area = float(input("Please enter your circle area: "))
    radius = math.sqrt(circle_area / math.pi)
    circle_circumference = 2 * math.pi * radius
    sphere_area = 4 * math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    printCalculations(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()


def startWithSphereArea():
    sphere_area = float(input("Please enter your sphere area: "))
    radius = math.sqrt(sphere_area / (4 * math.pi))
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * (radius ** 2)
    sphere_volume = (4 / 3) * math.pi * (radius ** 3)
    printCalculations(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()

def startWithSphereVolume():
    sphere_volume = float(input("Please enter your sphere volume: "))
    radius = ((3 * sphere_volume) / (4 * math.pi)) ** (1/3)
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * (radius ** 2)
    sphere_area = 4 * math.pi * (radius ** 2)
    printCalculations(radius, circle_circumference, circle_area, sphere_area, sphere_volume)
    continue_condition()

def printMenu():
    print("1) Radius")
    print("2) Circle Circumference")
    print("3) Circle Area")
    print("4) Sphere Area")
    print("5) Sphere volume")

def start_program():
    introduction_CircleAndSphere()
    print("Which circle or sphere calculation would you like to start with?")
    printMenu()
    option = int(input())
    if option == 1:
        startWithRadius()
    elif option == 2:
        startWithCircumference()
    elif option == 3:
        startWithCircleArea()
    elif option == 4:
        startWithSphereArea()
    else:
        startWithSphereVolume()

def printCalculations(radius, circle_circum, circle_area, sphere_area, sphere_volume):
    print(f"The radius of the circle is {radius}")
    print(f"The circumference of the circle is {circle_circum}")
    print(f"The area of the circle is {circle_area}")
    print(f"The area of the sphere is {sphere_area}")
    print(f"The volume of the sphere is {sphere_volume}")

def continue_condition():
    print("Would you like to play the game again?")
    answer = input("Please enter (yes/no) ")
    if answer == "yes":
        os.system('cls||clear')
        start_program()
    else: 
        return print("Goodbye!")

start_program()
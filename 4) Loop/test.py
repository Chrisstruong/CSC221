def introduction():
    print('This is a blueprint of the project. There are three functions.')
    print('These functions work together to solve the problem.')
    print('This sample uses the random number generator.')
def generate6DiceThrows():
    import random # import random module from Python Standard Library
global diceThrowNumber
diceThrowNumber = -1
while diceThrowNumber <= 0:
print('\nPlease enter positive number of dice throws you want.')
diceThrowNumber = int(input())
print('Global variables are visible from the time they are created')
print('until the end of the program. Here they are created and')
print('are visible in the print output method')
global dice_1
global dice_2
global dice_3
global dice_4
global dice_5
global dice_6
dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
dice_3 = random.randint(1,6)
dice_4 = random.randint(1,6)
dice_5 = random.randint(1,6)
dice_6 = random.randint(1,6)
count = 1
while count <= 6 :
number = random.randint(1,6)
print(number)
count += 1
def printOutput():
star = '*'
print(f' Dice number 1:{dice_1 * star}')
print('\n would you like to play it again?')
user_input = input(" Enter a character ('y' for yes): ")
global doItAgain
doItAgain = user_input[0]
introduction()
global doItAgain
doItAgain = 'y'
while(doItAgain =='y'):
generate6DiceThrows()
printOutput()

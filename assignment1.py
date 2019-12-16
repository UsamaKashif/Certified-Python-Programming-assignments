'''
1  Write a Python program to print the following string in a specific format
2  Write a Python program to get the Python version you are using
3  Write a Python program to display the current date and time.
4  Write a Python program which accepts the radius of a circle from the user
    and compute the area.
5  Write a Python program which accepts the user's first and last name and
    print them in reverse order with a space between them.
6  Write a python program which takes two inputs from user and print them
    addition
'''
import sys
import datetime
import math

def twinkleTwinkle():
    strings = ["Twinkle, twinkle, little star,","How I wonder what you are!","Up above the world so high,","Like a diamond in the sky."]
    print(strings[0])
    print(" ",strings[1])
    print("     ",strings[2])
    print("     ",strings[3])
    print(strings[0])
    print(" ",strings[1])


def pyVersion():    
    print("python version")
    print(sys.version)

def currentDateTime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("current date:",datetime.date.today())
    print("current time: ",current_time)


def circleArea():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius**2)
    print ("Area of the circle is:",round(area,2))


def reverseName():
    firstName = input("Enter your first name: ")
    firstName = [i for i in firstName[::-1]]
    fReversed = ''
    lastName = input("Enter your last name: ")
    lastName = [i for i in lastName[::-1]]
    lReversed = ''

    for i in firstName:
        fReversed += i

    for i in lastName:
        lReversed += i

    print(fReversed + " " + lReversed)


def addition():
    inputOne = input("Enter First Input: ")
    inputTwo = input("Enter Second Input: ")

    try:
        inputOne = int(inputOne)
        inputTwo = int(inputTwo)
        addition = inputOne + inputTwo
    except ValueError:
        addition = inputOne + inputTwo

    print(addition)

if __name__ == "__main__":
    twinkleTwinkle()
    print("----------------------------------------")
    pyVersion()
    print("----------------------------------------")
    currentDateTime()
    print("----------------------------------------")
    circleArea()
    print("----------------------------------------")
    reverseName()
    print("----------------------------------------")
    addition()


'''
1. Make a calculator using Python with addition , subtraction , multiplication ,
division and power.
2. Write a program to check if there is any numeric value in list using for loop
3. Write a Python script to add a key to a dictionary
4. Write a Python program to sum all the numeric items in a dictionary
5. Write a program to identify duplicate values from list
6. Write a Python script to check if a given key already exists in a dictionary
'''


def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1

def multiply(n1,n2):
    return n1*n2

def power(number, power):
    return number ** power

def div(n1,n2):
    if n1 == 0:
        return "division not possible"
    else:
        return n1/n2
def calculator(choice):
    if choice == "1":
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        print(add(num1,num2))
    elif choice == "2":
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        print(sub(num1,num2))
    elif choice == "3":
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        print(multiply(num1,num2))
    elif choice == "4":
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        print(div(num1,num2))
    elif choice == "5":
        num1 = int(input("enter the number: "))
        p = int(input("enter the power: "))
        print(power(num1,p))

def numericInList():
    myList = ["12abc","34","3bag43","apple","12","cherry"]
    numericValue = False
    for item in myList:
        if item.isnumeric():
            numericValue = True

    return numericValue


def addToDict():
    myDict = {"hello":"world", "python":"programming"}
    k = input("Enter the key: ")
    v = input("Enter the value: ")
    myDict[k] = v

    return myDict

def sumNumericinDict():
    myDict = {
        "value1": 32,
        "value2": "hello",
        "value3":23,
        "value4":"12"
    }
    sum = 0 
    for i in myDict.values():
        if type(i) == str and i.isnumeric():
            sum = sum + int(i)
        if type(i)==int:
            sum = sum + i 

    return sum

def duplicates():
    myList = ["hello","programming","hello","python","javascript","python"]
    dupli = []
    for item in myList:
        if item not in dupli:
            dupli.append(item)
        elif item in dupli:
            print(f'Duplicated item {item}')


def alreadyExists(x):
    dic = {
        1:30,
        4:12,
        6:19,
        3:29,
        2:87
    }

    if x in dic:
        print(f'The key, {x}, is present in the dictionaary')
    else:
        print(f'Key, {x}, is not present in the dictionary')


def main():
    print("1:  Make a calculator using Python with addition , subtraction , multiplication , division and power.")
    print("")
    print(" 1: add \n 2: subtract \n 3: multiply \n 4: divide \n 5: power")
    choice = input("Enter number between 1 and 5, inclusive: ")
    while not(choice >= "1" and choice<="5"):
        print("")
        choice = input("Enter number between 1 and 5, inclusive: ")

    calculator(choice)
    print("")

    print("2: Write a program to check if there is any numeric value in list using for loop")
    print(numericInList())
    print("")

    print("3: Write a Python script to add a key to a dictionary")
    print(addToDict())
    print("")

    print("4:  Write a Python program to sum all the numeric items in a dictionary")
    print(sumNumericinDict())
    print("")

    print("5: Write a program to identify duplicate values from list")
    duplicates()
    print("")

    print("6:  Write a Python script to check if a given key already exists in a dictionary")
    choice = int(input("Enter the key to check if it is present or not: "))
    alreadyExists(choice)

if __name__ == "__main__":
    main()
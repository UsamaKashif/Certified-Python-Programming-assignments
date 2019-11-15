def grades():
	count = 0
	total = 0
	while count < 5:
		grade = input(f'Enter marks for subject {count+1}: ')
		if grade.isdigit():
			count+=1
			total = total + int(grade)
		else:
			print("Enter numbers only..")


	if int(total)>=90:
		print("A*")
	elif int(total)>=80:
		print("A")
	elif int(total)>=70:
		print("B")
	elif int(total)>=60:
		print("C")
	elif int(total)>=50:
		print("D")
	else:
		print("Fail")
			

def evenOdd():
	valid = False
	while valid==False:
		number = input("Enter a number: ")
		if number.isdigit():
			valid = True
		else:
			print("Please enter a number..")

	if int(number) % 2 ==0:
		print("Even Number")
	else:
		print("Odd number")


def printLengthOfList():
	myList = [1,2,3,"python","java"]
	print("Printing the length of the list", myList)
	length = 0
	for i in myList:
		length += 1

	print(length)

def sumList():
	myList = [1,2,3,"python","java","javascript","34","43"]
	print("summing all the numbers from the list", myList)
	total = 0
	for i in myList:
		try:
			i = int(i)
			total = total + i
		except:
			pass


	print(total)


def largest():
	myList = [1,23,123,4,5,34,234,33,4,44]
	print("Printing largest number from the list", myList)
	largest = 0
	for i in myList:
		if i > largest:
			largest = i


	print (largest)

def lessThenFive():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	print("Printing number less than five from the list", a)
	num = 5
	for i in a:
		if i < num:
			print(i)


if __name__ == "__main__":
	grades()

	print("")

	evenOdd()

	print("")

	printLengthOfList()

	print("")

	sumList()

	print("")

	largest()

	print("")

	lessThenFive()



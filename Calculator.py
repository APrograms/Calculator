import math
print("Select an operation by typing the corresponding number:")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")
print("5 for Finding the square root")
print("6 for Finding the square")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The Sum of the two numbers is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The SDifference of the two numbers is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The Product of the two numbers is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The Ratio of the two numbers is " + str(int(num1) / int(num2)))
elif operation == "5":
    num1 = int(input("Enter number: "))
    print("The square root is %f " % (math.sqrt(num1)))
elif operation == "6":
    num1 = int(input("Enter number: "))
    print("The Square is %d " % (math.pow(num1, 2)))
else:
    print("Entered number is not a valid operation")

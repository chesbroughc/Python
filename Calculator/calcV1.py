import math  # import math for square root function

# determine which operation user wants to execute
answer = int(input("Please enter one of the following: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Square \n 6. Square Root \n"))

# ------------------------------------------ GET NUMBERS FROM USER FOR CALCULATION --------------------------------------------------------------------------------

if answer == 1:
    n1 = int(input("Enter the number you would like to add to.\n"))
    n2 = int(input("Enter the number you would like to add" + str(n1) + ".\n"))

elif answer == 2:
    n1 = int(input("Enter the number you would like to subtract from.\n"))
    n2 = int(input("Enter the number you would like to subtract " + str(n1) + ".\n"))

elif answer == 3:
    n1 = int(input("Enter the number you would like to multiply.\n"))
    n2 = int(input("Enter the number you would like to multiply" + str(n1) + "by.\n"))

elif answer == 4:
    n1 = int(input("Enter the number you would like to divide.\n"))
    n2 = int(input("Enter the number you would like to divide" + str(n1) + "by.\n"))

elif answer == 5:
    n1 = int(input("Enter the number you would like to square.\n"))

elif answer == 6:
    n1 = int(input("Enter the number you would like to find the square root of.\n"))

else:
    print("Your input was invalid, please try again.\n")

# ------------------------------------------ CALCULATION FUNCTIONS --------------------------------------------------------------------------------


def add(n1, n2):  # 1  Add
    a = n1 + n2
    return a


def subtract(n1, n2):  # 2  Subtract
    a = n1 - n2
    return a


def multiply(n1, n2):  # 3  Multiply
    a = n1 * n2
    return a


def divide(n1, n2):  # 4  Divide
    a = n1 / n2
    return a


def square(n1):  # 5  Square
    a = int(math.pow(n1, 2))
    return a


def squareRoot(n1):  # 6  Square Root
    a = math.sqrt(n1)
    a = int(a)
    return a


1

# ------------------------------------------ CONDITIONALS ----------------------------------------------------------------------------

if answer == 1:
    print(n1, "+", n2, " = ", add(n1, n2))

elif answer == 2:
    print(n1, "-", n2, " = ", subtract(n1, n2))

elif answer == 3:
    print(n1, "*", n2, " = ", multiply(n1, n2))

elif answer == 4:
    print(n1, "/", n2, " = ", divide(n1, n2))

elif answer == 5:
    print(n1, "^2 = ", square(n1))

elif answer == 6:
    print("The square root of " + str(n1) + " is " + str(squareRoot(n1)) + ".")

else:
    print("Your input was invalid, try again.\n")

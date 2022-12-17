import operators as op
y = 1
while y == 1:

    ans = input("""
    Choose: 
    1 = Addition
    2 = Subtraction
    3 = Multiplication
    4 = Division
    Enter choice here: """)
    z = 1

    if ans == '1':
        try:
            print("\nAddition:")
            n1 = int(input("Num1: = "))
            n2 = int(input("Num2: = "))
            x = op.add(n1, n2)
            print("The answer is: ", x)
        except Exception:
            print("Error occurred")
        else:
            print("No Error")
    elif ans == '2':
        try:
            print("\nSubtraction:")
            n1 = int(input("Num1: = "))
            n2 = int(input("Num2: = "))
            x = op.subtract(n1, n2)
            print("The answer is: ", x)
        except Exception:
            print("Error occurred")
        else:
            print("No Error")
    elif ans == '3':
        try:
            print("\nMultiplication:")
            n1 = int(input("Num1: = "))
            n2 = int(input("Num2: = "))
            x = op.mul(n1, n2)
            print("The answer is: ", x)
        except Exception:
            print("Error occurred")
        else:
            print("No Error")
    elif ans == '4':
        try:
            print("\nDivision:")
            n1 = int(input("Num1: = "))
            n2 = int(input("Num2: = "))
            x = op.div(n1, n2)
            print("The answer is: ", x)
        except Exception:
            print("Error occurred")
        else:
            print("No Error")
    else:
        print("Choose 1,2,3,4 only")
        z = 1

    while z == 1:
        z = input("Do you want to try again (Y/N)? ").lower()

        if z == 'y':
            y = 1
        elif z == 'n':
            y = 0
            print("Thank you!")
            break
        elif z != 'y' or x != 'n':
            z = 1
            print("Try again Y or N only")
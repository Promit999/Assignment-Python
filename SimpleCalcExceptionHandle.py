num1 = float(input("Enter the first number: ",))
op = input("Please Enter the operation: +, -, *, /")
num2 = float(input("Enter the second number: "))

if op == '+':
    print(str(num1) + "+" + str(num2) + "=" + str(num1 + num2))
elif op == "-":
    print(str(num1) + "-" + str(num2) + "=" + str(num1 - num2))
elif op == "*":
    print(str(num1) + "*" + str(num2) + "=" + str(num1 * num2))
elif op == "/":
    try:
        print(str(num1) + "/" + str(num2) + "=" + str(num1 / num2))
    except ZeroDivisionError as e:
        print("You cannot divide by zero")
        print(str(e))
    except ValueError as e:
        print("Please only enter numeric values")
        print(str(e))
num1 = float(input("Enter the first number: "))
op = input("Please Enter the operation: +, -, *, /\n")
num2 = float(input("Enter the second number: "))

if op == '+':
    print(str(num1) + "+" + str(num2) + "=" + str(num1 + num2))
elif op == "-":
    print(str(num1) + "-" + str(num2) + "=" + str(num1 - num2))
elif op == "*":
    print(str(num1) + "*" + str(num2) + "=" + str(num1 * num2))
elif op == "/":
    if num2 != 0:
        print(str(num1) + "/" + str(num2) + "=" + str(num1 / num2))
    else:
        print("You cannot divide by zero")
var1 = float(input("Enter the first number: "))
var2 = float(input("Enter the second number: "))
var3 = float(input("Enter the third number: "))

if (var1 >= var2) and (var1 >= var3):
    largest = var1
elif(var2 >= var1) and (var2 >= var3):
    largest = var2
elif(var3 >= var1) and (var3 >= var2):
    largest = var3

print("The largest among " + str(var1) + ", " + str(var2) + " and " + str(var3) + " is : " + str(largest))
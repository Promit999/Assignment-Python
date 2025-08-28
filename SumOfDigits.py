x = int(input("Enter the number: \n"))
summd = 0
while x > 0:
    ld = x % 10
    summd += ld
    x //= 10
print("The sum of digits is: " + str(summd))

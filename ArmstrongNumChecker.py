x = int(input("Enter the number: \n"))
countx = x
original = x
summ = 0
count = 0
while countx > 0:
    countx = countx // 10
    count +=1
if countx == 0:
    while x > 0:
        ld = x % 10
        print("last digit: " + str(ld))
        summ += ld ** count
        print("sum: " + str(summ) + " count: " + str(count))
        x = x // 10
        print("x: " + str(x))
    if summ == original:
        print("the number: " + str(original) + " is an armstrong number")
    elif summ != original:

        print("the number: " + str(original) + " is not an armstrong number")

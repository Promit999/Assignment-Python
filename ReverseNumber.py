n = int(input("Enter the number you want to reverse: "))
rnum = 0
ldigit = 0
while n >0:
    ldigit = n % 10
    rnum = rnum * 10 + ldigit
    n //= 10
print(rnum)
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))


if (x > 0) and (y > 0):
    quadrant = "belongs to 1st quadrant"
elif (x < 0) and (y < 0):
    quadrant = "belongs to 3rd quadrant"
elif (x < 0) and (y > 0):
    quadrant = "belongs to 2nd quadrant"
elif (x > 0) and (y < 0):
    quadrant = "belongs to 4th quadrant"
elif (x > 0) and (y == 0) or (x < 0) and (y == 0) :
    quadrant = "lies on the X axis"
elif (x == 0) and (y > 0) or (x == 0) and (y < 0):
    quadrant = "lies on the Y axis"
elif (x == 0) and (y == 0):
    quadrant = "lies on the origin"

print("The number: "+ str(x) + " of X axis and the number: "+ str(y) + " of Y axis : " + str(quadrant) )
c = float(input("Enter value in celsius: "))
f = (c * (9/5)) + 32
k = c + 273.15
if (c > 0):
    print("the value is above 0 degree celsius, converting to Fahrenheit. the value is: " + str(f) + " Fahrenheit.")
elif (c < 0 ):
    print("the value is below 0 degree celsius, converting to Kelvin. the value is: " + str(k) + " Kelvin.")
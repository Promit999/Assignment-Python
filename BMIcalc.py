h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in Kilograms: "))
BMI = w / (h**2)
if (BMI < 18.5):
    print("Your BMI is: " + str(BMI) + " Which is below 18.5, that means you are underweight")
elif (18.5 <= BMI <= 24.9):
    print("Your BMI is: " + str(BMI) + " Which is between 18.5 and 24.9, that means your waight is normal")
elif (25 <= BMI <= 29.9):
    print("Your BMI is: " + str(BMI) + " Which is between 25 and 29.9, that means you are overweight")
elif (BMI >= 30):
    print("Your BMI is: " + str(BMI) + " Which is over 30, that means you are obese")
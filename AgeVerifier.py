age = int(input("Enter age: "))

if 0 <= age <= 1:
    L = "an Infant"
elif 2 <= age <= 3:
    L = "a Toddler"
elif 4 <= age <= 12:
    L = "a Child"
elif 13 <= age <= 19:
    L = "a Teenager"
elif age >= 20:
    L = "an Adult"
print("You are " + L )
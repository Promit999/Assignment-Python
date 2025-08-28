pas = "#Adib123@"
i = 0
while i < 3:
    ui = str(input("Enter your password: "))
    if pas == ui:
        print("Unlocked")
        break
    else:
        print("Wrong Password, try again")
    i += 1 # Why doesn't the syntext i++ work????
    if i == 3:
        print("Account Locked, Contact Customer Support")
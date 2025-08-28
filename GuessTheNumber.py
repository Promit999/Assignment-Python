r = 8
while True:
    ui = int(input("Guess the number from 1  to 10: \n"))
    if r == ui:
        print("Congratulations!!! you guessed the number correctly")
        break
    elif r < ui:
        print("Sorry, you guessed too high, try again")
    elif r > ui:
        print("Sorry, you guessed too low, try again")

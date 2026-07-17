Secret_Number = 7

Attempts = 5
while Attempts > 0:
    User = int(input("Guess the secret number:"))
    if User == Secret_Number:
        print("Congratulations you are correct!")
        break
    else:
        print("Wrong guess")
        Attempts = Attempts - 1
        print("You have", Attempts,"more, try again")
else:
    print("Game Over")
    
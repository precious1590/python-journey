
Attempts = 3

while Attempts > 0:
    User = int(input("Enter pin:"))
    if User != 1234:
        print('Invalid Pin')
    else:
        print('Access Granted!')
        break
    Attempts = Attempts - 1
    print("Attempts left:", Attempts)
else:
    print("Card Blocked")

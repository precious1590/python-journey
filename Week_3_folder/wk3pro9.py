
for attempt in range(3,0,-1):
    password = int(input("enter password:"))


    if password == 1234:
        print("welcome!")
        break
    else:
        print("Your have",attempt-1, "left try again")
    if attempt == 1:
     print("Card Blocked")


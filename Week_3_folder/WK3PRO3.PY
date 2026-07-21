

for Number in range(1,4):
    Pin = int(input("Enter your pin:"))
    if Pin == 1234 :
        print("Access Granted")
        break
    else:
        print("Invalid pin")

    if Number == 3:
        print("Card Blocked")
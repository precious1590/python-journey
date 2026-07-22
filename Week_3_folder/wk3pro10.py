counter = 0
for Voters in range(5):
    name = input("Name:")
    if not name :
        print("Your name is required!")
    else:
        age = int(input("Age:"))
        if age < 18:
            print("Too young to vote")
        else:
            print("Eligible!")
            counter = counter +1

print("total eligible to vote:",counter)

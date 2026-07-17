Fuel = 120
while Fuel > 0:
    print("Available liter:",Fuel)
    Customer = int(input("How many Liters are you buying:"))
    if Customer <= 0:
            print("Please enter a valid fuel quantity.")
    elif Customer <= Fuel:
        print("proceed to make payment")
        print("Fuel sold")   ##this is just assuming the payment went through although i think i can merge this with the atm work after i get this right.
        Fuel = Fuel - Customer
        print("Available liter:",Fuel)
        
    else:
        print("Not enough Fuel")
else:
    print('Station Closed')
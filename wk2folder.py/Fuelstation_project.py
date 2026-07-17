Fuel = 120
while Fuel > 0:
    print("Available liter:",Fuel)
    Customer = int(input("How many Liters are you buying:"))
    if Customer <= 0:
            print("Please enter a valid fuel quantity.")
    elif Customer <= Fuel:
        print("proceed to make payment")
        Atm_pin = int(input("Enter pin:"))
        if Atm_pin == 1234:
            print('Access Granted')
            Total_bal = int(input("what is your total balance"))
            Amount = 1000 * Customer
            if Amount <= Total_bal:
                 Total_bal = Total_bal - Amount
                 print("Fuel Payment Deduced,",Amount, "balence:",Total_bal)
                 print("Fuel sold")   ##this is just assuming the payment went through although i think i can merge this with the atm work after i get this right.
                 Fuel = Fuel - Customer
                 print("Available liter:",Fuel)
        
            else:
                 print ("low funds please top up")                
        else:
            print('Invalid Pin')
       
    else:
        print("Not enough Fuel")
else:
    print('Station Closed')
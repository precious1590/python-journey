fuel = 100
for _ in range(5):
    customer = int(input("How much fuel do you want:"))
    if fuel == 0:
        print("NO MORE FUEL!")
        break
    elif customer > fuel:
        print("Not enough fuel to complet this order! The current fuel available is",fuel)
    
    else:
        print("Purchased")
        fuel = fuel- customer
   

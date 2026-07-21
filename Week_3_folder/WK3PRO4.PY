total_bill = 0
for items in range(1,6):
    grocery = int(input("Enter grocery price:"))
    
    total_bill = total_bill + grocery
print("your total bill is", total_bill)
discount = total_bill * 0.05
if total_bill > 10000:
        print("Congratulations! A 5% discount has been applied. Your new  total is ",total_bill-discount)

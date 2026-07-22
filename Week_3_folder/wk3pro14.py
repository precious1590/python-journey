even_number = 0
odd_number = 0
for number in range(10):
    User = int(input("Enter number:"))
    if User % 2 != 0:
        print("Odd Number")
        odd_number = odd_number + 1
    else:
        print("Even number")
        even_number = even_number + 1
print("The total even numbers:",even_number)
print("The total odd numbers:",odd_number)
   
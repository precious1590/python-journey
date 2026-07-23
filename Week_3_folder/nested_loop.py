#Basic NESTED LOOP 

for row in range(3):
   print("Row", row)

   for col in range(2):
       print(row, col)


for _ in range(3):
    for star in range(5):
        print("*", end="")


for number in range(1,6):
    for star in range(number):
        print("*", end="")
    print()

for number in range(5,0,-1):
    for star in range(number):
        print("*", end="")
    print()
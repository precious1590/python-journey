counter =0
for entry in range(5):
    student_name= input("Enter full name:")
    if not student_name :
        print("Name is required")
    else:
        print("Student Registered!")
        counter =counter +1
print ("Total number of registered student:",counter)
    
print ("Hello Day 1")
message = "Hello Day 1"
print (message)
name = 'komolafe precious'
print (name.title())
print  (name.upper())
print(name.lower())
first_name = 'precious'
last_name = 'komolafe'
full_name = f"{first_name} {last_name}"
full_name_1 = last_name + ' ' + first_name
print (full_name_1.title())
message = f" Hello, {full_name.title()}"
print (message)
print("o----")
print(" ||||")
exam_score = int(input("Enter exam score:"))
if exam_score >= 70 :
    print("EXCELLENT")
elif  exam_score >=50:
    print("Pass")
else:
    print('FAIL')
name = input("What is your name: ")
password = input("Enter password: ")

if name == "Precious" and password == "python123":
    print("WELCOME")
else:
    print("Invalid login")
Age = int(input("state your age:"))
Country = input('state your nationality:')
if Age >=18 and Country == "Nigeria":
    print("Eligible to vote")
else :
    print("not eligible")

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":

    full_name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    waec_score = int(input("Enter your WAEC score: "))
    nationality = input("Enter your nationality: ")
    birth_cert = input("Do you have a birth certificate? (yes/no): ")
    passport_photo = input("Do you have a passport photograph? (yes/no): ")
    state = input("Which state are you from? ")

    if not full_name:
        print("Name is required.")

    elif age < 16:
        print("Not eligible due to age.")

    elif nationality != "Nigerian":
        print("Only Nigerian applicants are accepted.")

    elif waec_score < 50:
        print("Admission denied due to low score.")

    else:
        if birth_cert == "yes" and passport_photo == "yes":
            print("Congratulations!")
            print("You are eligible for admission.")
        else:
            print("You passed the requirements but your documents are incomplete.")

        if waec_score >= 80:
            print("Excellent Candidate")
        elif waec_score >= 60:
            print("Average Candidate")
        else:
            print("Minimum Requirement Met")

        if state == "Abuja" or state == "Lagos":
            print("Priority Admission Candidate")
        else:
            print("Regular Admission Candidate")

else:
   print("Access Denied")
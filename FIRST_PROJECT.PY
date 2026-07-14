Username = input("Enter Username:")
Password = input("Enter Password:")
Full_name = input("What is your name:")
Age = int(input("State your age:"))
Nationality = input("What is yourrffr Nationality:")
State = input("what state are you from:")
Gender = input("pick your gender Mr Mrs or Ms:")
Waec_Score = int(input("WAEC score:"))
Birth_cert = input("Do you have a bith certificate:")
Pass_port = input ("Do you have a passport:")


if Username =="admin" and Password == "python123":
    if  not Full_name :
       print("Name is required")
    if Age < 18 :
       print("Not eligible due to age")
    if Nationality == "Nigeria":

        if Waec_Score >= 90:
            print("Outstanding Candidate, 50% discount applied")
        elif Waec_Score >=75:
            print("Excellent Candidate 30% Discount appllied")
        elif Waec_Score >=50 :
            print("Eligible")
        else :
            print("Admission denied due to low score")
        if State == "Lagos" or State == "Abuja":
                print(" Congratulations!! 5% special discount applied")
        if Birth_cert == "yes" and Pass_port == "yes":
            if Waec_Score >=75:
                print("PROFILE SUMMARY")
                print('FULL NAME:',Gender, Full_name)
                print('Age:',Age,)
                print("WAEC SCORE:",Waec_Score,)
                print('STATE:', State,)
                print("Congratulation you are eligible for a scholarship")
            else:
                print('PROFILE SUMMARY')
            print('FULL NAME:',Gender, Full_name)
            print('Age:',Age)
            print("WAEC SCORE:",Waec_Score)
            print('STATE:',State) 
        else:
            print("Document incomplete")
    
           
    else:
        print("Only Nigerians are accepted")             
else:
    print("Access Denied")
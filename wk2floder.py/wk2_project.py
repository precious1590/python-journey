Username = input("Username:")
password = input("password")

if Username == "admin" and password == "python123":
    print("Welcome admin!")
    Admission_number = 20
    while Admission_number > 0:
         Fullname = input('FULLNAME:')
         Age = int(input("Age:"))
         Gender = input("Select your gender (MR/MRS/MS):")
         Nationality = input ('Nationality:')
            

         if not Fullname :
                print("name is required")
         else:        
                if Age >= 18:
                        
                        if Nationality != "nigerian":
                            print("Only Nigerians are eligible for enrollment")    
                        else:
                            State = input("state:")
                            Waec_score = int(input("WAEC SCORE:"))
                            Birth_cert = input("Do you have your birth certificate:")
                            Passport = input("Do you have a passport:")
                            if Birth_cert == "yes" and Passport ==   "yes":
                                if Waec_score >= 90:
                                    print(" Outstanding + 50% Scholarship")
                                elif Waec_score >=75 :
                                    print(" Excellent + 30% Scholarship")
                                elif Waec_score >= 50:
                                    print("Eligible")
                                else :
                                    print('Admission Denied')
                                if State == "Lagos" or State == 'Abuja':
                                    print("5% special discount")
                            else:
                                print("Birth certificate and passport are require to complete application")
                else:
                        print("Age must be at least 18")
                Admission_number = Admission_number - 1
                admin = input("Do you want to admit another student:")
                if admin == "No":
                    break
else:
    print('Access Denied')

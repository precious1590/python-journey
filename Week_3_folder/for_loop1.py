pass_count = 0
fail_count = 0
for score in range(1,6):
    result = int(input("Enter score",score,":"))
    if result >=70:
        print("Pass")
        pass_count = pass_count + 1
        
    else:
        print("Fail")
        fail_count = fail_count + 1
print("Total Pass:", pass_count)
print("Total Fail:", fail_count)

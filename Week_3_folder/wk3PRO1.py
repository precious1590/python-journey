# PROJECT 1: Student Score Analyzer
# 19-07-2026

pass_percentage = 0
Pass = 0
fail_percentage = 0
Fail = 0

for student in range(1, 6):
    score = int(input("Enter Student score: "))

    if score >= 70:
        print("Pass")
        Pass = Pass + 1
        pass_percentage = pass_percentage + 20

    else:
        print("Fail")
        Fail = Fail + 1
        fail_percentage = fail_percentage + 20

print("Total Passes:", Pass)
print("Total Fails:", Fail)
print("Pass Percentage:", pass_percentage, "%")
print("Fail Percentage:", fail_percentage, "%")
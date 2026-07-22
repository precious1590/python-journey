outstanding = 0
excellent = 0
eligible = 0
denied = 0

for number in range(5):
    waec_score = int(input("Enter WEAC score:"))
    if waec_score >= 90:
        print("Outstanding!")
        outstanding = outstanding +1
    elif waec_score >=80 :
        print("Excellent!")
        excellent = excellent+1
    elif waec_score >=50:
        print("Eligible!")
        eligible = eligible+1
    else:
        print("Denied")
        denied = denied+1
print("GRAND TOTAL",
      "OUTSTANDING:",outstanding,
      "EXCELLENT:",excellent,
      "ELIGIBLE:",eligible,
      "DENIED:",denied)




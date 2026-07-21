Total_score = 0
Average = 0

for Score_count in range(1,6):
    score = int(input("Enter score: "))
    Total_score = Total_score + score
Average = Total_score // 5
print("Total Score: ",Total_score)
print("AVERAGE SCORE:",Average)
    

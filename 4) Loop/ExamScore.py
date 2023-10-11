# 2) Write a program to read a list of exam scores given as integer percentages in the range 0 to 100

# Input list of scores
score_list = list(map(int, input("Enter a list of exam scores given as integer percentages in the range 0 to 100: ").split(' ')))
score_length = len(score_list)

A_total, B_total, C_total, D_total, F_total = 0, 0, 0, 0 ,0
total = 0

highest = 0
lowest = 100

for score in score_list:
    total += score
    # Find lowest and highest
    if score > highest:
        highest = score
    elif score < lowest:
        lowest = score
    # Find grade types
    if score >= 90:
        A_total += 1
    elif score >= 80 and score < 90:
        B_total += 1
    elif score >= 70 and score < 80:
        C_total += 1
    elif score >= 60 and score < 70:
        D_total += 1
    else:
        F_total += 1
    
average = round(total / score_length, 1)

# Output
print()
print(f"Total number of scores = {len(score_list)}")
print(f"Number of A's = {A_total}, {round((A_total / score_length) * 100)}%")
print(f"Number of B's = {B_total}, {round((B_total / score_length) * 100)}%")
print(f"Number of C's = {C_total}, {round((C_total / score_length) * 100)}%")
print(f"Number of D's = {D_total}, {round((D_total / score_length) * 100)}%")
print(f"Number of F's = {F_total}, {round((F_total / score_length) * 100)}%")
print(f"Lowest score is {lowest}")
print(f"Highest score is {highest}")
print(f"Average score is {average}")
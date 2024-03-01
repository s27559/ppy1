# Define variable
score = float(input("Enter your score: "))

# Determine the grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

if grade == "A":
    grade = "5"
elif grade == "B":
    grade = "4"
elif grade == "C":
    grade = "3"
elif grade == "D":
    grade = "2"
else:
    grade = "1"

# Print the grade
print("Your grade is:", grade)
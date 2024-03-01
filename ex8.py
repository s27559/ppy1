######### ex1
name = input("input name: ")
surname = input("input surname: ")
age = input("input age: ")
print("Hello, " + name + " " + surname + " " + age + "!")

######### ex2
fahr = float(input("input temperature in fahrenheit: "))
cels = (fahr - 32) * (5/9)
print("temperature in celsius: ", cels)

######### ex3
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

######### ex4
num1 = int(input("first number: "))
num2 = int(input("second number: "))

if (num1 % num2) == 0:
    result = "divisable"
else:
    result = "indivisable"

print(num1, "is", result, "by", num2)

######### ex6
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1>side2:
    longest = side1
else:
    longest = side2

if longest<side3:
    longest = side3

if (side1 + side2) > longest and (side3 == longest):
    possible = "can"
elif (side1 + side3) > longest and (side2 == longest):
    possible = "can"
elif (side2 + side3) > longest and (side1 == longest):
    possible = "can"
else:
    possible = "can\'t"

print("the triangle",possible,"be drawn")

######### ex7
# Define variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "dividing by 0"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

# Print the result
print("Result:", result)
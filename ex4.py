num1 = int(input("first number: "))
num2 = int(input("second number: "))

if (num1 % num2) == 0:
    result = "divisable"
else:
    result = "indivisable"

print(num1, "is", result, "by", num2)
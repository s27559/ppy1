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
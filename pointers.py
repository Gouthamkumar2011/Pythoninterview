num1 = 11 
num2 = num1

print ("before num2 is updated")
print("num1 = ", num1)
print("num2 = ", num2)

print("\n num1 points to:", id(num1))
print(" num2 points to:", id(num2))


num2 = 22

print ("after num2 is updated")
print("num1 = ", num1) 
print("num2 = ", num2)
print("\n num1 points to:", id(num1))
print(" num2 points to:", id(num2))

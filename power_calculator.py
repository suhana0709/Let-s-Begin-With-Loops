num1 = int(input("Enter the number: "))
num2 = int(input("Enter the power: "))
to_the_power = ""
for i in range(1, num2 + 1):
     to_the_power = num1 ** i
print("Answer = ",to_the_power)
num = int(input("Enter a number: "))
a = num
b = 0
while a > 0:
    a= a // 10
    b = b +1

print("There are",b, " digits in the number ",num)
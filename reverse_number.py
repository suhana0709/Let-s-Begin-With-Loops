#input number greater than 1
n = int(input("Enter the value of n: "))

#printing the statement "number fron n to 1"
print("Numbers form {0} to {1} are: ".format(n,1))

#loop to print numbers
for i in range(n, 0, -1):
    print(i)
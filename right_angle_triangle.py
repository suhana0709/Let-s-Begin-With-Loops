print("A pattern of right angle triangle with stars(*)")
#taking input
n = int(input("Enter the number of rows: "))
#outer loop for handling rows
for i in range(n):
    #inner loop for handling coloums
    for j in range(i+1):
        #display result
        print("*", end="")
    print()
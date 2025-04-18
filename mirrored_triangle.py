print("A pattern of upsidedown right angle triangle with stars(*)")
#taking input
n = int(input("Enter the number of rows: "))
#outer loop for handling rows
for i in range (n, 0, -1):
     #inner loop for handling coloums
    for j in range(i):
        #display result
        print("*", end="")
    print()
#taking input from the user
rows = int(input("Please enter the Total Number of Rows: "))
num = 1 #initialize
print("\n _Floyd's Triangle_")
#outer loop for coloums
for i in range (1, rows+1):
    for j in range(1, i+1):
        #display result
        print(num, end=' ')
        num = num+1
    print()
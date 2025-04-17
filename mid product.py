num = int(input("Enter the number: "))
t = num
numLen = 0

# Count the number of digits
while t > 0:
    numLen += 1
    t = int(t / 10)

# Check if the number has 4 or more digits
if numLen >= 4:
    midOne = midTwo = 0
    chk = 0
    t = num

    # Calculate the positions of the middle digits
    mid1_pos = numLen // 2 - 1
    mid2_pos = numLen // 2

    while t > 0:
        rem = t % 10
        if chk == mid1_pos:
            midTwo = rem
        elif chk == mid2_pos:
            midOne = rem
        t = int(t / 10)
        chk += 1

    prod = midOne * midTwo
    print("\nProduct of Mid digits (" + str(midOne) + " * " + str(midTwo) + ") = ", prod)
else:
    print("\nIt's not a 4 or more than 4-digit number!")

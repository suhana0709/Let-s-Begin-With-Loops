#taking input
string = str(input("Enter a word: "))
#taking input of the character
char = str(input("Give the character which you want to check: "))
i = 0
count = 0
#starting a loop
while (i < len(string)):   #string operation

    if(string[i] == char):
        count = count+1
    i = i+1
print("There are ",count," characters in ",string)
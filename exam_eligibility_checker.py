#taking input from the student that he can enter the exam or not
medical_cause = str(input("Did you have any medical cause Y or N: "))
#taking input for the attendence
atten = int(input("Enter your attendence: "))
#checking the input and predincting the output
if medical_cause == 'Y':
    print("Allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("You are not allowed.")
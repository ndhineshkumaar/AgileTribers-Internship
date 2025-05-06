score=float(input("Enter the score: "))
if score>=90 and score<=100:
    print("Grade: A \nStatus: Pass")
elif score>=80 and score<=89:
    print("Grade: B \nStatus: Pass")
elif score>=70 and score<=79:
    print("Grade: C \nStatus: Pass")
elif score>=60 and score<=69:
    print("Grade: D \nStatus: Fail")
else:
    print("Grade: F \nStatus: Fail")
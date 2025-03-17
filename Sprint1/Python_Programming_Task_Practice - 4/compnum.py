def compnum(num1,num2):
    if num1==num2:
        print("Both are equal")
    elif num1>num2:
        print(num1, "is larger")
    else:
        print(num2, "is larger")



num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
compnum(num1,num2)
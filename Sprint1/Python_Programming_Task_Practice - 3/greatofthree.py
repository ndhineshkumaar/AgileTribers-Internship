#trying using if,else conditions
def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("The greatest number is: ",num1)
    elif num2>num1 and num2>num3:
        print("The greatest number is: ",num2)
    else:
        print("The greatest number is: ",num3)

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
greatest(num1,num2,num3)

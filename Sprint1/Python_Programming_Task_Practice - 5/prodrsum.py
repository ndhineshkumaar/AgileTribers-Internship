def prodrsum(a,b):
    if (a*b)>500:
        return a+b
    else: return a*b



num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
print(prodrsum(num1,num2))
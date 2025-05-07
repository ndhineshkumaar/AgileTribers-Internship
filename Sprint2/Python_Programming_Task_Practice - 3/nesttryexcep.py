def nesttry():
    try:
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
        result=num1/num2
        print(result)
    except ZeroDivisionError:
        print("Division using zero is not possible")
    except ValueError:
        print("Check the value entered")
    else:
        print("Operation successful")

nesttry()
def posoRNeg(num):
    if num<0:
        print("Negative")
    elif num>0:
        print("Positive")
    else:
        print("neither positive nor negative")


num=int(input("Enter the number"))
posoRNeg(num)
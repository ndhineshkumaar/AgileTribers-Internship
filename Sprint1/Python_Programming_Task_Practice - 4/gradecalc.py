def gradecalc(mark):
    if 90<=mark<=100:
        print("A")
    elif 80<=mark<=89:
        print("B")
    elif 70<=mark<=79:
        print("C")
    elif 60<=mark<=69:
        print("D")
    else:
        print("F")



mark=int(input("Enter the marks "))
gradecalc(mark)
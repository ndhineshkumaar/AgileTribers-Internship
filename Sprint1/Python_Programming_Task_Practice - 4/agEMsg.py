def agemsg(age):
    if age<16:
        print("You can't drive.")
    elif 16<=age<=17:
        print("You can drive but not vote")
    elif 18<=age<=24:
        print("You can vote but not rent a car")
    else:
        print("You can do pretty much anything")



age=int(input("Enter your age "))
agemsg(age)
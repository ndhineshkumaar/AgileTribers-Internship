def main():
    try:
        num=int(input("Enter the number: "))
        str=input("Enter the str: ")
        strtonum=int(str)
        div=num/num
        print(f"The converted int: {strtonum} \nThe ans after dividing is {div}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except ValueError:
        print("Converting given string to int is not possible")

main()
try:
    num=int(input("Enter the number "))
except ValueError:
    print("Invalid Input")
else:
    print(f"Conversion Success. \n The number is {num}")

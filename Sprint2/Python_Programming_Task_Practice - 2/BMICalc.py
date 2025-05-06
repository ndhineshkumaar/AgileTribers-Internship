weight=float(input("Enter the weight (in kg) : "))
height=float(input("Enter the height (in m) : "))
BMI = weight / ( height ** 2 )
if BMI<18.5:
    print(f"BMI: {BMI:.2f}\nCategory: Underweight")
elif BMI>=18.5 and BMI<=24.9:
    print(f"BMI: {BMI:.2f}\nCategory: Normal weight")
elif BMI>=25 and BMI<=29.9:
    print(f"BMI: {BMI:.2f}\nCategory: Overweight")
else:
    print(f"BMI: {BMI:.2f}\nCategory: Obesity")
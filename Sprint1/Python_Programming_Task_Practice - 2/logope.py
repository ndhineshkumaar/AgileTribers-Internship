is_student= True
is_Employee= False

if is_student and is_Employee:
    print("You are a student and an employee")
elif is_student or is_Employee:
    print("You are either a student or an employee")
elif not is_student:
    print("You are not a student")
elif not is_Employee:
    print("You are not an employee")
employees = {
 'E001': {'name': 'Alice', 'department': 'HR', 'salary': 50000},
 'E002': {'name': 'Bob', 'department': 'IT', 'salary': 60000},
 'E003': {'name': 'Charlie', 'department': 'Finance', 'salary': 55000}
}

def get_salary(employee_dict, emp_id):
    if emp_id in employee_dict:
        print("Salary of the given Emp ID :",employee_dict[emp_id]['salary'])
    else:
        print("EMP ID does not exist")

def increase_salary(employee_dict, percentage):
    for i in employee_dict:
        empname=employee_dict[i]['name']
        incsalary=((percentage/100)*(employee_dict[i]['salary']))+(employee_dict[i]['salary'])
        print("The Salary of ",empname, " after increasing ",percentage," is ", incsalary)

id= input("Enter the EMP ID : ")
per=10
get_salary(employees, id)
increase_salary(employees,per)
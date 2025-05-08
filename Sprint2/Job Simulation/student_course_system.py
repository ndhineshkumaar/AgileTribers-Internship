import os

courses_available = ("Python", "Data Science", "Web Development", "AI & ML")
students_file = "Sprint2/Job Simulation/students.txt"
students_data = {}

#fee formatting

def format_currency(amount):
    return f"₹{amount:,.2f}"

#saving the student details on the txt file

def save_all_students():
    with open(students_file, "w") as file:
        for s_id, student_detail in students_data.items():
            course_str = ",".join(student_detail['Course'])
            line = f"{s_id}|{student_detail['Name']}|{student_detail['Age']}|{course_str}|{student_detail['Total Fee']}|{student_detail['Fee Paid']}|{student_detail['Balance']}\n"
            file.write(line)


#loading data from the txt file
def load_from_file():
    try:
        if not os.path.exists(students_file):
            return
        with open(students_file,"r") as f:
            for line in f:
                parts=line.strip().split('|')
                s_id,name,age=parts[0],parts[1],parts[2]
                course=set(parts[3].split(','))
                total,paid,balance=parts[4],parts[5],parts[6]
                students_data[s_id]={"Name":name,"Age":age,"Course":course,"Total Fee":float(total),"Fee Paid":float(paid),"Balance":float(balance)}
            print("Loaded")
    except FileNotFoundError:
        print("Error: File does not exist..")
    except Exception as e:
        print(f"Error loading the file: {e}")

#adding student details

def add_student():
    try:
        s_id = (input("Enter the Student ID: "))
        if str(s_id) in students_data:
            raise Exception("The Student ID already exist..")
        
        name=input("Enter the Student Name: ")
        age=int(input("Enter the student age: "))
        if age <= 0:
            raise ValueError("Age must be a positive number.")
        
        print("Select a Course from the below list:")
        for i in range(len(courses_available)):
            print(f"{i+1}. {courses_available[i]}")

        choices = input("Enter course choices separated by commas: ").split(",")
        selected_courses = [courses_available[int(choice.strip()) - 1] for choice in choices]

        total = float(input("Enter Total Fees: "))
        paid = float(input("Enter Fees Paid: "))
        if paid > total:
            raise ValueError("Fee paid cannot be more than total fees.")
        
        balance = total - paid
        students_data[s_id]={"Name":name,"Age":age,"Course":selected_courses,"Total Fee":float(total),"Fee Paid":float(paid),"Balance":float(balance)}

        save_all_students()
        print("Student details added successfully")

    except ValueError as ve:
        print(f"Error: {ve}")
    except IndexError:
        print("Invalid course selection.")
    except Exception as e:
        print(f"Unexpected error: {e}")

#viewing students detailss

def view_students():
    if not students_data:
        print("No student data exists..")
        return
    for s_id,details in students_data.items():
        print(f"Student ID: {s_id}")
        print(f"Name: {details["Name"]}")
        print(f"Age: {details["Age"]}")
        print(f"Course enrolled {', '.join(details["Course"])}")
        print(f"Total Fee: {format_currency(details['Total Fee'])}")
        print(f"Fee Paid: {format_currency(details['Fee Paid'])}")
        print(f"Balance Fee: {format_currency(details['Balance'])}\n")
    
#To update the details of existing student information

def update_student():
    s_id = input("Enter the Student ID to update: ")
    if s_id not in students_data:
        print("Student ID does not exist.")
        return
    try:
        name = input("Enter the Student Name: ")
        age = int(input("Enter the student age: "))
        if age <= 0:
            raise ValueError("Age must be a positive number.")

        print("Select a Course from the below list:")
        for i, course in enumerate(courses_available, 1):
            print(f"{i}. {course}")

        choices = input("Enter course choices separated by commas: ").split(",")
        selected_courses = [courses_available[int(choice.strip()) - 1] for choice in choices]

        total = float(input("Enter Total Fees: "))
        paid = float(input("Enter Fees Paid: "))
        if paid > total:
            raise ValueError("Fee paid cannot be more than total fees.")

        balance = total - paid
        students_data[s_id] = {
            "Name": name,
            "Age": age,
            "Course": selected_courses,
            "Total Fee": total,
            "Fee Paid": paid,
            "Balance": balance
        }

        save_all_students()
        print("Student details edited successfully.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except IndexError:
        print("Invalid course selection.")
    except Exception as e:
        print(f"Unexpected error: {e}")

#to remove the students details

def remove_student() :
    s_id=input("Enter the Student Id to remove: ")
    if s_id in students_data:
        del(students_data[s_id])
    else:
        print("Student ID does not exist")
        return
    save_all_students()
    print("Student details removed successfully")

def generate_fee_report():
    print("\nStudents with Pending Fee Payments:")
    for sid, info in students_data.items():
        if info['Balance'] > 0:
            print(f"{sid} - {info['Name']} | Balance: {format_currency(info['Balance'])}")

def main():
    load_from_file() #loading file
    while True:
        print("""
---- Student Course Management ----
1. Enroll a Student
2. View All Student Records
3. Update Student Information
4. Remove a Student Record
5. Generate Fee Report
6. Exit
""")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                update_student()
            elif choice == 4:
                remove_student()
            elif choice == 5:
                generate_fee_report()
            elif choice == 6:
                print("Thank You")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()

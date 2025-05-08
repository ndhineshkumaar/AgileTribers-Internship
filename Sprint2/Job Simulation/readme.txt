STUDENT COURSE MANAGEMENT SYSTEM
================================

PROJECT OVERVIEW:
-----------------
This project is a console-based Python application designed as part of a job simulation to manage student enrollments, course registrations, fee payments, and generate reports. It demonstrates core Python concepts such as file handling, exception handling, data structures, and string formatting.

KEY FEATURES:
-------------
1. Enroll a Student
   - Collects student details including ID, name, age, selected courses, and fee information.
   - Validates input and stores data in a structured format using a dictionary.
   - Prevents duplicate course entries using a set.

2. View All Student Records
   - Displays all student data loaded from a text file.
   - Outputs details in a readable and formatted manner using f-strings and currency formatting.

3. Update Student Information
   - Allows modifications to a student's existing record using their ID.
   - Updates are saved persistently to the file.

4. Remove a Student Record
   - Deletes a student entry based on ID and updates the data file accordingly.

5. Generate Fee Report
   - Lists students who have outstanding balance fees with formatted currency values.

DATA STORAGE:
-------------
- Student records are stored in a text file (`students.txt`) located at:
  `Sprint2/Job Simulation/students.txt`
- Each record is saved in a pipe-separated format:
  `ID|Name|Age|Course1,Course2|Total Fee|Fee Paid|Balance`

COURSES AVAILABLE:
------------------
- Python
- Data Science
- Web Development
- AI & ML

TECHNICAL IMPLEMENTATION:
--------------------------
- Exception Handling:
  - Manages invalid input, file access errors, and logical errors such as fee overpayments.

- File Handling:
  - Reads from and writes to `students.txt` using standard file I/O operations.
  - Supports both full save and load functionality.

- String Formatting:
  - Outputs currency values using `₹` and formatted with two decimal places.

- Data Structures Used:
  - Dictionary for student data
  - List for course selection
  - Set for unique course entries
  - Tuple for predefined course options

HOW TO RUN:
-----------
1. Ensure Python 3 is installed on your system.
2. Place `student_course_system.py` in your working directory.
3. Create the necessary folder path (`Sprint2/Job Simulation/`) or update the `students_file` path in the script.
4. Run the script using: `python student_course_system.py`
5. Use the menu to interact with the system.

AUTHOR:
-------
[Dhinesh Kumaar N]


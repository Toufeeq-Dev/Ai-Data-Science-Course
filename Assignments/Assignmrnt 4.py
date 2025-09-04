                            # SRMS using nested list
                            
student_records = []

# 1. Add Student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter Student roll no: ")
    course = input("Enter student course: ")
    marks = int(input("Enter student marks: "))

    student = [name, roll_no, course, marks]
    student_records.append(student)
    print("Student added Successfully\n")

# 2. Display All Students
def display_records():
    if student_records:
        print("----------------------")
        print("Students Record")
        print("----------------------")

        for student in student_records:
            print(f"Name: {student[0]}")
            print(f"Roll No: {student[1]}")
            print(f"Course: {student[2]}")
            print(f"Marks: {student[3]}")
            print("----------------------")
    else:
        print("No Record Found.........")

# 3. Search Student by Roll Number
def search_student():
    if not student_records:
        print("No records to search.\n")
        return None, None

    roll_no = input("Enter the roll number you want to search: ")

    for index, student in enumerate(student_records):
        if student[1] == roll_no:
            return student, index

    print("Student with this roll number not found....")
    return None, None

# 4. Update Marks
def update_marks():
    student_found, index = search_student()
    if student_found is not None:
        print("---------------")
        print("Record Found")
        print("---------------")
        print(f"Name: {student_found[0]}")
        print(f"Roll No: {student_found[1]}")
        print(f"Course: {student_found[2]}")
        print(f"Marks: {student_found[3]}")
        print("---------------")

        new_marks = int(input("Enter marks to update: "))
        student_records[index][3] = new_marks
        print("Record Successfully updated...\n")
    else:
        print("Record not Found! Unable to update\n")

# 5. Delete Student
def delete_record():
    student_found, index = search_student()
    if student_found is not None:
        student_records.pop(index)
        print("Record deleted successfully.\n")
    else:
        print("Record not found! Unable to delete\n")

# 6. Sort Students by Marks
def sort_records():
    if student_records:
        student_records.sort(key=lambda x: x[3], reverse=True)
        print("Records sorted by marks successfully.\n")
    else:
        print("No records to sort.\n")

# Main Menu
while True:
    print("-----------------------------")
    print("1. Add Student Record.")
    print("2. Display Student Records.")
    print("3. Search Student Record.")
    print("4. Update Student Record.")
    print("5. Delete Student Record.")
    print("6. Sort Records")
    print("7. Exit")
    print("-----------------------------")

    option = input("Enter your option: ")

    if option == '1':
        add_student()
    elif option == '2':
        display_records()
    elif option == '3':
        student, _ = search_student()
        if student:
            print("------ Student Found ------")
            print(f"Name: {student[0]}")
            print(f"Roll No: {student[1]}")
            print(f"Course: {student[2]}")
            print(f"Marks: {student[3]}")
            print("---------------------------\n")
    elif option == '4':
        update_marks()
    elif option == '5':
        delete_record()
    elif option == '6':
        sort_records()
    elif option == '7':
        print("Exiting the program... Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.\n")


# SRMS using list of Dictioinery

student_records = []  

# 1. Add Student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter Student roll no: ")
    course = input("Enter student course: ")
    marks = int(input("Enter student marks: "))

    student = {
        'name': name,
        'roll_no': roll_no,
        'course': course,
        'marks': marks
    }
    student_records.append(student)
    print("Student added Successfully\n")

# 2. Display All Students
def display_records():
    if student_records:
        print("----------------------")
        print("Students Record")
        print("----------------------")

        for student in student_records:
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            print(f"Course: {student['course']}")
            print(f"Marks: {student['marks']}")
            print("----------------------")
    else:
        print("No Record Found.........")

# 3. Search Student by Roll Number
def search_student():
    if not student_records:
        print("No records to search.\n")
        return None, None

    roll_no = input("Enter the roll number you want to search: ")

    for index, student in enumerate(student_records):
        if student['roll_no'] == roll_no:
            return student, index

    print("Student with this roll number not found....")
    return None, None

# 4. Update Marks
def update_marks():
    student_found, index = search_student()
    if student_found is not None:
        print("---------------")
        print("Record Found")
        print("---------------")
        print(f"Name: {student_found['name']}")
        print(f"Roll No: {student_found['roll_no']}")
        print(f"Course: {student_found['course']}")
        print(f"Marks: {student_found['marks']}")
        print("---------------")

        new_marks = int(input("Enter marks to update: "))
        student_records[index]['marks'] = new_marks
        print("Record Successfully updated...\n")
    else:
        print("Record not Found! Unable to update\n")

# 5. Delete Student
def delete_record():
    student_found, index = search_student()
    if student_found is not None:
        student_records.pop(index)
        print("Record deleted successfully.\n")
    else:
        print("Record not found! Unable to delete\n")

# 6. Sort Students by Marks
def sort_records():
    if student_records:
        student_records.sort(key=lambda x: x['marks'], reverse=True)
        print("Records sorted by marks successfully.\n")
    else:
        print("No records to sort.\n")

# Main Menu
while True:
    print("-----------------------------")
    print("1. Add Student Record.")
    print("2. Display Student Records.")
    print("3. Search Student Record.")
    print("4. Update Student Record.")
    print("5. Delete Student Record.")
    print("6. Sort Records")
    print("7. Exit")
    print("-----------------------------")

    option = input("Enter your option: ")

    if option == '1':
        add_student()
    elif option == '2':
        display_records()
    elif option == '3':
        student, _ = search_student()
        if student:
            print("------ Student Found ------")
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            print(f"Course: {student['course']}")
            print(f"Marks: {student['marks']}")
            print("---------------------------\n")
    elif option == '4':
        update_marks()
    elif option == '5':
        delete_record()
    elif option == '6':
        sort_records()
    elif option == '7':
        print("Exiting the program... Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.\n")

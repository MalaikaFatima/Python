
# ===================================
# Student Result Management System
# ===================================

def calculate_grade(percentage):
    """ This function calculate the grade based on the percentage """


    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_percentage(total_obtained, total_maximum):
    return (total_obtained / total_maximum) * 100



def result():
    """ This function is the main function of the program which takes input from the user and displays the result report card """
    
    name = input("Enter student name: ").strip()

    num_subjects = int(input("Enter number of subjects: "))
    max_marks = float(input("Enter maximum marks per subject: "))

    marks = []

    # Input marks for each subject
    for i in range(num_subjects):
        obtained = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(obtained)

    # Calculate total obtained and maximum marks
    total_obtained = sum(marks)
    total_maximum = num_subjects * max_marks

    # Calculate percentage and grade
    percentage = calculate_percentage(total_obtained, total_maximum)
    grade = calculate_grade(percentage)

    # Check student status

    if all(mark >= max_marks * 0.40 for mark in marks):
        status = "PASS"
    else:
        status = "FAIL"
        grade = "F"

    # Display report card
    print("\n========== RESULT REPORT ==========")
    print("Student Name:", name)
    print("Total Obtained:", total_obtained, "/", total_maximum)
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("Status:", status)
    print("===================================")



result()
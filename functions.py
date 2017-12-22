students = []


def get_student_titlecast():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = []
    students_titlecase = get_student_titlecast()
    print (students_titlecase)


def add_student(name, student_id=332):
    student ={"name":name , "student_id":student_id}
    students.append(student)


student_list = get_student_titlecast()

student_name = input("enter student name: ")
student_id = input("enter student_id: ")
add_student(student_name,student_id)

print_students_titlecase()


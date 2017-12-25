students = []


def get_student_titlecast():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = []
    students_titlecase = get_student_titlecast()
    print (students_titlecase)


def add_student(name, student_id=332):
    student ={"name":name , "student_id":student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("student.txt" , "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not save sile")


def read_file():
    try:
        f = open("student.txt" , "r")
        for student in read_student(f):
            students.append((student))
        f.close()
    except Exception:
        print("could not open sile")

def read_student(f):
    for line in f:
        yield line


read_file()
print(students)
#print_students_titlecase()
#student_name = input("enter student name: ")
#student_id = input("enter student_id: ")
#add_student(student_name,student_id)
#save_file(student_name)




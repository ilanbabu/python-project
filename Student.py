students = []
class Student:
    scool_name = "Zafririm"

    def __init__(self,name,student_id=332):
        self.name = name
        self.student_id  = student_id
        students.append(self)


    def __str__(self):
        return "Student: " + self.name


    def get_name_capitalize(self):
        return self.name.capitalize()


    def add_student(self,name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)


    def get_school_name(self):
        return self.scool_name

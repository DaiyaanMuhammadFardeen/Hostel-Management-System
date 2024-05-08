import os

from models.Student import Student
from services.StudentService import StudentService

studentService = StudentService()
class UI:
    def clearScreen(self):
        os.system("cls")

    username = str()
    password = str()
    def showLogin(self):
        self.clearScreen()
        print("Welcome to the Hostel Management System")
        print("Please login to continue")
        print("Username: ", end="")
        username = input()
        self.username = username
        print("Password: ", end="")
        password = input()
        self.password =  password

    def login(self):
        if self.username == "admin" and self.password == "123":
            self.adminMode()
        else:
            self.studentMode()

    def adminMode(self):
        self.clearScreen()
        print(
            """Welcome {{username}} to Hostel Management Portal.
            Please select one of the following options:
            1. Add Student
            2. Remove Student
            3. View Students
            4. Search Student
            
            """
        )
        choice = int(input("Option:"))
        match choice:
            case 1:
                self.addStudent()
            case 2:
                self.removeStudent()
            case 3:
                self.viewStudents()
            case 4:
                self.searchStudent()
            case _:
                self.adminMode()

    def addStudent(self):
        self.clearScreen()
        new_student = Student()
        new_student.name = input("Name: ")
        new_student.contact = input("Phone no: ")
        new_student.father = input("Father Name: ")
        new_student.mother = input("Mother Name: ")
        new_student.email = input("Email: ")
        studentService.addStudent(new_student)
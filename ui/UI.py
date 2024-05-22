import os

from models.Student import Student
from services.AdminService import AdminService
from services.StudentService import StudentService

adminService = AdminService()
studentService = StudentService()


class UI:
    def clearScreen(self):
        os.system("clear")

    username = str()
    password = str()

    def welcome(self):
        self.clearScreen()
        print("Welcome to the Hostel Management System")
        print("Please login to continue")

    def showLogin(self):
        print("Username: ", end="")
        username = input()
        self.username = username
        print("Password: ", end="")
        password = input()
        self.password = password

    def login(self):
        self.welcome()
        self.showLogin()
        if self.username == "admin" and self.password == "123":
            self.adminMode()
        else:
            self.studentMode()

    def adminMode(self):
        self.clearScreen()
        print(
            f"""Welcome {self.username} to Hostel Management Portal.
            Please select one of the following options:
            1. Add Student
            2. Remove Student
            3. View Students
            4. Search Student
            5. Logout
            6. Exit
            
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
            case 5:
                self.logout()
            case 6:
                exit()
            case _:
                self.adminMode()

    def addStudent(self):
        self.clearScreen()
        new_student = Student()
        new_student.name = input("Name: ")
        new_student.username = input("Username: ")
        new_student.password = input("Password: ")
        new_student.student_id = input("StudentID (last 4 digits): ")
        new_student.contact = input("Phone no: ")
        new_student.father = input("Father Name: ")
        new_student.mother = input("Mother Name: ")
        new_student.email = input("Email: ")
        adminService.addStudent(new_student)
        self.adminMode()

    def removeStudent(self):
        self.clearScreen()
        student_id = input("Student ID: ")
        adminService.removeStudent(student_id)
        self.adminMode()

    def viewStudents(self):
        self.clearScreen()
        adminService.viewStudents()
        self.adminMode()
        pass

    def searchStudent(self):
        self.clearScreen()
        student_id = input("Student ID: ")
        adminService.searchStudent(student_id)
        self.adminMode()

    def studentMode(self):
        self.clearScreen()
        print(
            f"""Welcome {self.username} to Hostel Management Portal.
            Please select one of the following options:
            1. See dues
            2. Update Profile
            3. Logout
            4. Exit

            """
        )
        choice = int(input("Option:"))
        match choice:
            case 1:
                self.seeBalance()
            case 2:
                self.updateProfile()
            case 3:
                self.logout()
            case 4:
                exit()
            case _:
                self.studentMode()

    def logout(self):
        self.username = None
        self.password = None
        self.clearScreen()
        self.login()

    def seeBalance(self):
        studentService.showBalance(self.username)

    def updateProfile(self):
        updated_Student = Student()
        updated_Student.name = input("Updated Name: ")
        updated_Student.contact = input("Updated Phone no: ")
        updated_Student.father = input("Updated Father Name: ")
        updated_Student.mother = input("Updated Mother Name: ")
        updated_Student.email = input("Updated Email: ")
        studentService.updateProfile(updated_Student, self.username)

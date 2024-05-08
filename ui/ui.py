import os

class UI:
    def clear(self):
        os.system("cls")

    username = str()
    password = str()
    def showLogin(self):
        self.clear()
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
        self.clear()
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
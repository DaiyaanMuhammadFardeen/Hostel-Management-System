import pandas as pd


class AdminRepository:
    def __init__(self):
        self.studentDB = pd.read_csv("db/student_db.csv")
        self.studentDB.set_index("id", inplace=True)
        # self.userDB = pd.read_csv("db/user_db.csv")
        # self.userDB.set_index("id", inplace=True)

    def addStudent(self, new_student):
        studentDict = {
            "id": new_student.student_id,
            "name": new_student.name,
            "contact": new_student.contact,
            "father": new_student.father,
            "mother": new_student.mother,
            "email": new_student.email,
            "user_id": new_student.id,
        }
        userDict = {
            "user_id": new_student.id,
            "username": new_student.username,
            "password":  new_student.password,
            "role": "student",
        }
        self.studentDB = self.studentDB.append(studentDict, ignore_index=True)
        # self.userDB = self.userDB.append(userDict, ignore_index=True)
        self.studentDB.to_csv("db/student_db.csv", index=True)

    def removeStudent(self, student_id):
        self.studentDB.drop(student_id, inplace=True)
        self.studentDB.to_csv("db/student_db.csv", index=True)

    def allStudents(self):
        return self.studentDB

    def searchStudent(self, student_id):
        student = self.studentDB.iloc(student_id)
        return student

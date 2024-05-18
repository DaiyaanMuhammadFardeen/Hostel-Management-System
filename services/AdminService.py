from repositories.AdminRepository import AdminRepository

adminRepository = AdminRepository()


class AdminService:
    def addStudent(self, new_student):
        adminRepository.addStudent(new_student)
        print("Student Added")

    def removeStudent(self, student_id):
        adminRepository.removeStudent(student_id)
        print("Student Removed")

    def viewStudents(self):
        studentList = adminRepository.allStudents()
        # print("{Name}\t\t{Email}\t\t{Father Name}\t\t{Mother Name}\t\t{student.contact}")
        # for student in studentList:
        #     print(f"{student.name}\t\t{student.email}\t\t{student.father}\t\t{student.mother}\t\t{student.contact}\t\t")
        print(studentList)

    def searchStudent(self, student_id):
        student = adminRepository.searchStudent(student_id)
        print(f"{student.name}\t\t{student.email}\t\t{student.father}\t\t{student.mother}\t\t{student.contact}\t\t")

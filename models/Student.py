import uuid

from models.User import User


class Student(User):
    def __init__(self):
        super().__init__()
        self.student_id = ""
        self.name = ""
        self.contact = ""
        self.father = ""
        self.mother = ""
        self.email = ""
        self.user_id = self.id

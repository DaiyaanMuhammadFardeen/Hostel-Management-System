import uuid

from models.User import User


class Student(User):
    id = str()
    name = str()
    contact = str()
    father = str()
    mother = str()
    email = str()
    user_id = uuid.uuid4()

import uuid

import User


class Student(User):
    id = int()
    name = str()
    contact = str()
    father = str()
    mother = str()
    email = str()
    user_id = uuid.uuid4()

import User

class Student(User):
    id = int()
    name = str()
    contact = str()
    father = str()
    mother = str()
    email = str()
    user_id = int()
    def __init__(self,  id, name, contact, father, mother, email):
        self.id = id
        self.name = name
        self.contact = contact
        self.father = father
        self.mother = mother
        self.email = email
        self.user_id = User.get_user_id()

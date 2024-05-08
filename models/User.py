import uuid


class User:
    id = uuid.uuid4()
    username = str()
    password = str()
    role = str()


def get_user_id(self):
    return self.id


def get_user_username(self):
    return self.username

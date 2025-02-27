from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash

class User(UserMixin):

    def __init__(self, id,email,password,fullname=""):
        self.id = id
        self.email = email
        self.password = password
        self.fullname = fullname

    @classmethod
    def generate_hash(cls,password):
        return generate_password_hash(password)

    @classmethod
    def check_password(cls,hashed_password,password):
        return check_password_hash(hashed_password,password)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class BookStoreUser(db.Model):
    __tablename__ = 'BookStoreUser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    password = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40))
    age = db.Column(db.String(40))
    mobile = db.Column(db.String(40))

    def __init__(self, username, first_name, last_name, password, email, age, mobile):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.age = age
        self.mobile = mobile



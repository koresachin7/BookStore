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


class BookStore(db.Model):
    __tablename__ = 'BookStore'
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(40))
    book_author = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey(BookStoreUser.id))

    def __init__(self, book_title, book_author, user_id):
        self.book_title = book_title
        self.book_author = book_author
        self.user_id = user_id

    def json(self):
        return {"book_id": self.book_id, "book_title": self.book_title, "book_author": self.book_author,
                "user_id": self.user_id}

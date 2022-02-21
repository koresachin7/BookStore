from flask import Flask

from bookstore.models import db
from bookstore.users import user_app
# from bookstore.users_store import book_app

app = Flask(__name__)

app.register_blueprint(user_app)
# app.register_blueprint(book_app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/BookStore'
db.init_app(app)

from flask import Blueprint

book_app = Blueprint('book_app', __name__)


from bookstore.users_store import users_store_views


from flask import Blueprint

user_app = Blueprint('user_app', __name__)

from bookstore.users import user_views




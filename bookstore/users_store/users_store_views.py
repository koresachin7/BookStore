from bookstore import db
from flask import request, jsonify
from bookstore.models import BookStore
from bookstore.users_store import book_app


@book_app.route('/book_post', methods=['POST'])
def book_post():
    data = request.get_json()
    book_title = data.get('book_title')
    book_author = data.get('book_author')
    user_id = data.get('user_id')

    user_book = BookStore(book_title, book_author, user_id)
    db.session.add(user_book)
    db.session.commit()
    return jsonify({"message": "book is created "})


@book_app.route('/book_get', methods=['GET'])
def book_get():
    data = request.get_json()
    books = BookStore.query.filter_by(user_id=data.get('user_id')).all()
    return jsonify("book is list ", list(i.json() for i in books))


@book_app.route('/book_put', methods=['PUT'])
def book_put():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        book_id = data.get('book_id')
        book_validate = BookStore.query.filter_by(user_id=user_id, book_id=book_id).first()
        if book_validate:
            book_validate.book_title = data["book_title"]
            book_validate.book_author = data.get('book_author')
            db.session.add(book_validate)
            db.session.commit()
            return jsonify(" book update successfully", book_validate.json())
        else:
            return jsonify({"message": "book credentials invalid "})

    except Exception as e:
        return jsonify("user not existed", str(e))


@book_app.route('/book_delete', methods=['DELETE'])
def book_delete():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        book_id = data.get('book_id')
        book_validate = BookStore.query.filter_by(user_id=user_id, book_id=book_id).first()
        if book_validate:
            db.session.delete(book_validate)
            db.session.commit()
            return jsonify(" book delete successfully")
        else:
            return jsonify({"message": "book credentials invalid "})

    except Exception as e:
        return jsonify("user not existed", str(e))

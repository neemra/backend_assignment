import token_service
from flask import request, Blueprint
from model.admin import model_admin
from model.book_validation import book_validation

import db

admin_bp = Blueprint("library_admin","admin_services")

@admin_bp.route("/admin/accept-borrow-req",methods=["POST"])
@token_service.token_decrypt
def accept_borrow_req():

    data = request.get_json()
    db_conn = db.mysqlconnect()

    if not book_validation.is_valid(data):
        return {"result": "Invalid accept borrow request data. Please provide book_id."}

    book_id = data.get("book_id")
    result = model_admin.accept_borrow_request(book_id)
    db.disconnect(db_conn)
    return {"result": result}

@admin_bp.route("/admin/add-new-books",methods=["POST"])
@token_service.token_decrypt
def add_new_books():

    data = request.get_json()
    db_conn = db.mysqlconnect()

    book = model_admin.add_new_book(data)
    db.disconnect(db_conn)

    return book, "Book Added Sucessfully"


@admin_bp.route("/admin/marked-book-as-returned", methods=["POST"])
@token_service.token_decrypt
def marked_book_as_returned():

    data = request.get_json()
    db_conn = db.mysqlconnect()

    book_id = data.get("book_id")
    result = model_admin.mark_book_as_returned(book_id)
    db.disconnect(db_conn)

    return result, "Book is Returned"

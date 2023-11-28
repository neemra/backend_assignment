import token_service
from flask import request, Blueprint
from model.customers import model_customers
import db

customer_bp = Blueprint("library_customer","customer_services")

@customer_bp.route("/search-book",methods=["GET"])
@token_service.token_decrypt
def search_books():

    data = request.get_json()
    conn = db.mysqlconnect()
    search_term = data.get("search_term")
    books = model_customers.search_books(conn, search_term)
    db.disconnect(conn)
    return {
        "books": books
    }

@customer_bp.route("/borrow-req/<int:book_id>",methods=["POST"])
@token_service.token_decrypt
def req_to_borrow_book(book_id):

    data = request.get_json()
    conn = db.mysqlconnect()
    customer_id = data.get("customer_id")
    borrow_date_from = data.get("borrow_date_from")
    borrow_date_to = data.get("borrow_date_to")

    result = model_customers.request_to_borrow_book(book_id, customer_id, borrow_date_from, borrow_date_to)
    db.disconnect(conn)
    return {"result": result}
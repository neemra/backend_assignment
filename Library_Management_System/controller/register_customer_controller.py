import token_service
from flask import request, Blueprint
from model.customers import model_customers, customer_validation
import db

reg_customer_bp = Blueprint("register_customer","reg_customer_services")

@reg_customer_bp.route("/register-customer",methods=["POST"])
@token_service.token_decrypt
def register_customer():
    data = request.get_json()
    conn = db.mysqlconnect()

    # Validate customer data
    if not model_customers.is_valid_customer_data(data):
        return {"result": "Invalid customer data. Please provide name, email, and password."}

    customer_id = register_customer(data)
    db.disconnect(conn)
    return {"customer_id": customer_id}


@reg_customer_bp.route("/login-user",methods=["POST"])
@token_service.token_decrypt
def login_user():

    data = request.get_json()
    conn = db.mysqlconnect()
    
    # Validate login data
    if not model_customers.is_valid_login_data(data):
        return {"result": "Invalid login data. Please provide Valid email and password."}

    email = data.get("email")
    password = data.get("password")
    customer = model_customers.login_customer(email, password)

    if customer:
        db.disconnect(conn)
        return {"customer": customer}
    else:
        db.disconnect(conn)
        return {"result": "Invalid email or password."}

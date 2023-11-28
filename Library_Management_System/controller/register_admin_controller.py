import token_service
from flask import request, Blueprint
from model.admin import model_admin, admin_validation
import db

reg_admin_bp = Blueprint("register_admin","reg_admin_services")

@reg_admin_bp.route("/register/admin",methods=["POST"])
@token_service.token_decrypt
def register_admin():
    data = request.get_json()
    conn = db.mysqlconnect()

    # Validate customer data
    if not admin_validation.is_valid_data(data):
        return {"result": "Invalid customer data. Please provide name, email, and password."}

    customer_id = model_admin.register_admin(data)
    db.disconnect(conn)
    return "ADMIN ADDED SUCESSFULLY"


@reg_admin_bp.route("/admin/login-admin",methods=["POST"])
@token_service.token_decrypt
def login_admin():

    data = request.get_json()
    conn = db.mysqlconnect()
    
    # Validate login data
    if not admin_validation(data):
        return {"result": "Invalid login data. Please provide Valid email and password."}

    email = data.get("email")
    password = data.get("password")
    login = model_admin.login_admin(email, password)

    if login:
        db.disconnect(conn)
        return {"login": "LOGIN SUCESSFULLY"}
    else:
        db.disconnect(conn)
        return {"result": "Invalid email or password."}
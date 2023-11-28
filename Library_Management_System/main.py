from flask import Flask
from controller.admin_controller import admin_bp 
from controller.customer_controller import customer_bp 
from controller.register_admin_controller import reg_admin_bp 
from controller.register_customer_controller import reg_customer_bp



app = Flask(__name__)

app.register_blueprint(admin_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(reg_admin_bp)
app.register_blueprint(reg_customer_bp)


if __name__  == "__main__":
    app.run(
        debug=True,
        port=4000
    )

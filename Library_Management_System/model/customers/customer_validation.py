def is_valid_customer_data(data):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    return name and email and password and not email.isspace()

def is_valid_login_data(data):
    
    email = data.get("email")
    password = data.get("password")

    return email and password and not email.isspace()
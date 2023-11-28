
def is_valid_data(data):
    
    email = data.get("email")
    password = data.get("password")

    return email and password and not email.isspace()
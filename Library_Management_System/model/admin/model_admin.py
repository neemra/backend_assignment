def register_admin(db_conn, data):
    query = """
            INSERT INTO libraryms.admin (email, password) 
            VALUES (%(email)s, %(password)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "email": data.get("email"),
            "password": data.get("password"), 
        }
    )
    db_conn.commit()
    return cur.lastrowid



def login_admin(db_conn, email, password):
    query = """
            SELECT id, email FROM libraryms.admin 
            WHERE email = %(email)s AND password = %(password)s
            """
    cur = db_conn.cursor()
    cur.execute(query, {"email": email, "password": password})
    return cur.fetchone()

def add_new_book(db_conn, data):
    query = """
            INSERT INTO libraryms.books (title, description, category) 
            VALUES (%(title)s, %(description)s, %(category)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "title": data.get("title"),
            "description": data.get("description"),
            "category": data.get("category"),
        },
    )
    db_conn.commit()
    return cur.lastrowid


def accept_borrow_request(db_conn, book_id):
    query = """
            UPDATE libraryms.books 
            SET is_borrowed = TRUE 
            WHERE id = %(book_id)s AND is_borrowed = FALSE
            """
    cur = db_conn.cursor()
    cur.execute(query, {"book_id": book_id})
    db_conn.commit()
    return cur.rowcount


def mark_book_as_returned(db_conn, book_id):
    query = """
            UPDATE libraryms.books 
            SET is_borrowed = FALSE, 
            borrower_id = NULL, 
            borrow_date_from = NULL, 
            borrow_date_to = NULL, 
            return_date = NOW()
            WHERE id = %(book_id)s AND is_borrowed = TRUE
            """
    cur = db_conn.cursor()
    cur.execute(query, {"book_id": book_id})
    db_conn.commit()
    return cur.rowcount

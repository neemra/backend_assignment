def register_customer(db_conn, data):

    query = """
            INSERT INTO libraryms.customer (id, name, email, password) 
            VALUES (%(name)s, %(email)s, %(password)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "name": data.get("name"),
            "email": data.get("email"),
            "password": data.get("password"),  
        }
    )
    db_conn.commit()
    return cur.lastrowid


def login_customer(db_conn, email, password):
    query = """
            SELECT id, name, email FROM libraryms.customer 
            WHERE email = %(email)s AND password = %(password)s
            """
    cur = db_conn.cursor()
    cur.execute(query, {"email": email, "password": password})
    return cur.fetchone()


def search_books(db_conn, search_term):
    query = """
            SELECT id,
            title, 
            description, 
            category 
            FROM libraryms.books 
            WHERE title LIKE %(search_term)s OR description LIKE %(search_term)s OR category LIKE %(search_term)s
            """
    cur = db_conn.cursor()
    cur.execute(query, {"search_term": f"%{search_term}%"})
    return cur.fetchall()


def request_to_borrow_book(db_conn, book_id, customer_id, borrow_date_from, borrow_date_to):
    
    #Validation check
    
    if is_book_borrowed(book_id):
        return {"result": "Book is already borrowed or not found."}
    
    query = """
            UPDATE libraryms.books 
            SET is_borrowed = TRUE, borrower_id = %(customer_id)s, borrow_date_from = %(borrow_date_from)s, borrow_date_to = %(borrow_date_to)s
            WHERE id = %(book_id)s AND is_borrowed = FALSE
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "book_id": book_id,
            "customer_id": customer_id,
            "borrow_date_from": borrow_date_from,
            "borrow_date_to": borrow_date_to,
        },
    )
    db_conn.commit()
    return cur.rowcount

def is_book_borrowed(db_conn, book_id):
    
    query = """
            SELECT is_borrowed
            FROM libraryms.books 
            WHERE id = %(book_id)s
            """
    cur = db_conn.cursor()
    cur.execute(
        query, 
        {
            "book_id": book_id
            }
        )
    book_status = cur.fetchone()
    db_conn.close()
    return book_status and book_status["is_borrowed"]



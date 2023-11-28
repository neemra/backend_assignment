import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="pakistan 1",
        db='libraryms',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn
    
# To close the connection
def disconnect(conn):
  conn.close()

# Driver Code
if __name__ == "__main__":
    mysqlconnect()
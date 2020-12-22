import sqlite3

conn = sqlite3.connect('./data/customers.db', check_same_thread=False)
c = conn.cursor()

def create_user_table():
    c.execute('''CREATE TABLE IF NOT EXISTS CUSTOMERS
             (ID INT,
              NAME TEXT,
              EMAIL TEXT);''')
    return True

def create_reviews_table():
    c.execute('''CREATE TABLE IF NOT EXISTS REVIEWS
             (ID INT,
              REVIEWERID INT,
              STARS INT,
              REVIEW TEXT);''')
    return True


def insert_user(id, name, email):
    sql = '''INSERT INTO CUSTOMERS (ID, NAME, EMAIL)
             VALUES (?, ?, ?)'''
    c.execute(sql, (id, name, email))
    conn.commit()

def insert_review(id, reviewerid, stars, review):
    sql = '''INSERT INTO REVIEWS (ID, REVIEWERID, STARS, REVIEW)
             VALUES (?, ?, ?, ?)'''
    c.execute(sql, (id, reviewerid, stars, review))
    conn.commit()

def update_user_email(id, email):
    id = "%" + id + "%"
    email = "%" + email + "%"
    c.execute('UPDATE CUSTOMERS SET EMAIL = ? WHERE ID = ?', (email, id,))
    conn.commit()

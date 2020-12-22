import sqlite3

conn = sqlite3.connect('./data/customers.db', check_same_thread=False)
c = conn.cursor()


def create_user_table():
    c.execute('''CREATE TABLE IF NOT EXISTS CUSTOMERS
             (ID INT,
              NAME TEXT,
              EMAIL TEXT,
              PASSWORD TEXT);''')
    return True


def create_reviews_table():
    c.execute('''CREATE TABLE IF NOT EXISTS REVIEWS
             (ID INT,
              REVIEWERID INT,
              SHOPID, INT
              RATING INT,
              REVIEW TEXT);''')
    return True


def insert_user(id, name, email, password):
    sql = '''INSERT INTO CUSTOMERS (ID, NAME, EMAIL, PASSWORD)
             VALUES (?, ?, ?, ?)'''
    c.execute(sql, (id, name, email, password))
    conn.commit()


def insert_review(id, reviewerid, shopid, rating, review):
    sql = '''INSERT INTO REVIEWS (ID, REVIEWERID, SHOPID, RATING, REVIEW)
             VALUES (?, ?, ?, ?)'''
    c.execute(sql, (id, reviewerid, shopid, rating, review))
    conn.commit()


def update_user_email(id, email):
    c.execute('UPDATE CUSTOMERS SET EMAIL = ? WHERE ID = ?', (email, id,))
    conn.commit()


def update_user_pass(id, password):
    c.execute('UPDATE CUSTOMERS SET PASSWORD = ? WHERE ID = ?', (password, id,))
    conn.commit()

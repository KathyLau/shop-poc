import sqlite3

conn = sqlite3.connect('./data/suggestedShops.db', check_same_thread=False)
c = conn.cursor()

table_name = '''suggestedShops'''


def create_sugg_table():
    c.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name + '''
             (ID INT,
              NAME TEXT,
              IMAGE TEXT,
              WEBSITE TEXT,
              SERVICE TEXT,
              LOCATION TEXT,
              TYPE TEXT);''')
    return True


def insert(id, name, image, website, service, location, type):
    sql = '''INSERT INTO suggestedShops (ID, NAME,
          IMAGE, WEBSITE, SERVICE, LOCATION, TYPE)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''
    c.execute(sql, (id, name, image, website, service, location, type))
    conn.commit()


def countSuggestionsInDB():
    c.execute('''SELECT COUNT(*) FROM suggestedShops''')
    num = c.fetchall()[0][0]
    return num

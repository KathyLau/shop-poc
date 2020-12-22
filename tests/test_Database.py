import sqlite3
from utils.store import create_sugg_table, insert, countSuggestionsInDB
from utils.setup import selectshopbyname, selectshops, selectshopbyid, updateshopbyname, updateshopbyservice  # noqa: E501

conn = sqlite3.connect('./data/suggestedShops.db', check_same_thread=False)
c = conn.cursor()


def test_suggTableMade():
    """ Tests the create_sugg_table method by checking if the table exists
    """

    create_sugg_table()
    c.execute('SELECT name FROM sqlite_master WHERE type = ? AND name = ?',
              ('table', 'suggestedShops',))
    result = c.fetchone()[0]
    if result == "suggestedShops":
        print("passed test 1")
    else:
        print("failed test 1")


def test_insertSuggestion():
    """ Inserts a new row to suggestions table then checks if last inserted
        record matches it. If it passes, it deletes the extra record
    """

    # get ID of last record
    c.execute('SELECT max(id) from suggestedShops')
    x = c.fetchone()[0]
    id = x+1
    # increments by 1
    # inserts new record using ID and fake inputs
    insert(id, "FakeNameRestaurantTester", "Image", "website.com",
           "fakeservice", "fakeplace", "restaurant")
    # Gets last inserted record
    sql_st = '''SELECT * FROM suggestedShops WHERE id = (SELECT max(id) FROM suggestedShops)''' # noqa
    c.execute(sql_st)
    name = c.fetchone()[1]
    """
    checks if name on last inserted record matches the
    name of record that we just tried to insert
    """
    if name == "FakeNameRestaurantTester":
        print("passed test 2")
        # removes the added row after test passes
        c.execute('DELETE FROM suggestedShops WHERE name  LIKE ?', ('%FakeNameRestaurantTester%',)) # noqa
        conn.commit()
    else:
        print("failed test 2")


def test_countSugg_insert():
    """ Tests insert and countSuggestionsInDB methods concurrently
    """

    original = countSuggestionsInDB()

    c.execute('SELECT max(id) from suggestedShops')
    max_id = c.fetchone()[0]
    id = max_id + 1
    insert(id, "FakeNameRestaurantTester", "Image", "website.com",
           "fakeservice", "fakeplace", "restaurant")

    after = countSuggestionsInDB()

    difference = after - original
    if difference == 1:
        print("passed test 3")
        c.execute('DELETE FROM suggestedShops WHERE name  LIKE ?',
                  ('%FakeNameRestaurantTester%',))
        conn.commit()
    else:
        print("failed test 3")
        c.execute('DELETE FROM suggestedShops WHERE name  LIKE ?',
                  ('%FakeNameRestaurantTester%',))
        conn.commit()


def test_selectShopName():
    """ Tests if selectShopName can accurately select a shop given a name.
    """

    term = "Jamaica Breeze"
    lower_term = term.lower()
    results = selectshopbyname(lower_term)
    # checks if index and name of record pulled match the searched term
    if results[0][0] == 234 and results[0][1] == "Jamaica Breeze":
        print("passed test 4")
    else:
        print("failed test 4")


def test_selectShop():
    """ Tests selectShop() to see if it will pull the same amount of records given
        a substring and the full string of a unqiue search term
    """

    term = "Queens"
    lower_term = term.lower()
    results = selectshops(lower_term)
    original = len(results)

    substring_term = "Qu"
    lower_substring = substring_term.lower()
    substring_results = selectshops(lower_substring)
    substr = len(substring_results)

    difference = substr - original

    if difference == 0:
        print("passed test 5")
    else:
        print("Failed test 5")


def test_updateShopName():
    """ Tests updateshopbyname() to see if it will change the name given id"""

    id = 10
    shop = selectshopbyid(id)
    oldname = shop[1]
    newname = "Smthing"

    updateshopbyname(id, newname)

    shop = selectshopbyid(id)
    assert(shop[1] == newname)

    updateshopbyname(id, oldname)


def test_updateShopService():
    """ Tests updateshopbyservice() to see if it will change
        the service given id
    """

    id = 10
    shop = selectshopbyid(id)
    oldservice = shop[4]
    newservice = "sit in only"

    updateshopbyservice(id, newservice)

    shop = selectshopbyid(id)
    assert(shop[4] == newservice)

    updateshopbyservice(id, oldservice)


test_suggTableMade()
test_insertSuggestion()
test_countSugg_insert()
test_selectShopName()
test_selectShop()
test_updateShopName()
test_updateShopService()

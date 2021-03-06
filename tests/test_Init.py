# import the method from project folder
from .map import inc
from .map import searchbar
from .map import dist
from .map import borough
from .map import Biz


# this is a sample test from prof paine's project
def test_inc():
    """ Tests the increment function

    Parameters
    ----------
    none
    """

    assert inc(1) == 2, "did not pass test_inc"


# below are some possible test ideas to use on ""code"" in map.py

# test 1 - checks if a string is taken in from the searchbar - should
# always end up being a string

def test_searchbar():
    """ Tests the search bar method

    Parameters
    ----------
    none
    """

    searchedvalue = isinstance(searchbar(), str)
    if searchedvalue:
        print("Pass test 1")
    else:
        print("Fail test 1")


# test 2 - check if any duplicates in list of shops


def anydup(thelist):
    """ Checks if there are any duplicates in the list of buisnesses

    Parameters
    ----------
    thelist : List
        List of Biz objects
    """

    seen = set()
    for x in thelist:
        if x in seen:
            print("Fail test 2")
        seen.add(x)
    return print("Pass test 2")


# test 3 - check if a searched value for distance is an int
def test_dist():
    """ Tests if function to ensure distance is an integer works

    Parameters
    ----------
    none
    """

    distvalue = isinstance(dist(), int)
    if distvalue:
        print("Pass test 1")
    else:
        print("Fail test 1")


# test 4 - check if list is empty
def emptyList(thelist):
    """ Checks if list is empty

    Parameters
    ----------
    thelist : List
        List of Biz objects
    """

    if not thelist:
        print("Fail test 3")
    else:
        print("Pass test 3")

# test 5 - check if searched value for borough is a string


def test_borough():
    """ Tests if function to ensure borough is a string is working

    Parameters
    ----------
    none
    """

    b = isinstance(borough(), str)
    if b:
        print("Pass test 1")
    else:
        print("Fail test 1")


# test 6 - check the actual value of the searchbar


def test2_searchbar():
    """ Test searchbar method

    Parameters
    ----------
    none
    """

    assert searchbar() == "poke restaurant"

# test 7 - check the actual distance of the search


def test_dist2():
    """ Tests function that check if distance value is integer

    Parameters
    ----------
    none
    """

    assert dist() == 500


# test 8 - check if the borough actually matches
def test_borough2():
    """ Tests borough function in map.py

    Parameters
    ----------
    none
    """
    assert borough() == "Brooklyn"


# test 9 - test Biz class creation
def test_Bizclass():
    """ Tests if Biz Class creation
    Parameters
    ----------
    none
    """

    p1 = Biz("Westside", "Morningside Heights", "Grocery store")
    if isinstance(p1, Biz):
        print("Pass test 9")
    else:
        print("Fail test 9")


# test 10 - test Biz class comparison
def test_Bizes():
    """ Tests Biz Class comparison

    Parameters
    ----------
    none
    """

    p1 = Biz("Westside", "Morningside Heights", "Grocery store")
    p2 = Biz("Up", "Morningside Heights", "Coffee shop")
    assert p1.location == p2.location


test_Bizes()

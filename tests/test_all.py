#import the method from project folder
from .map import inc
from .map import searchbar
from .map import dist
from .map import borough
from .map import Biz


#this is a sample test from prof paine's project
def test_inc():
    assert inc(1) == 2, "did not pass test_inc"

#below are some possible test ideas to use on ""code"" in map.py

#test 1 - checks if a string is taken in from the searchbar - should always end up being a string
def test_searchbar():
    searchedvalue = isinstance(searchbar(), str)
    if searchedvalue:
        print("Pass test 1")
    else:
        print("Fail test 1")

#test 2 - check if any duplicates in list of shops
def anydup(thelist):
  seen = set()
  for x in thelist:
    if x in seen: print("Fail test 2")
    seen.add(x)
  return print("Pass test 2")


#test 3 - check if a searched value for distance is an int
def test_dist():
    distvalue = isinstance(dist(), int)
    if distvalue:
        print("Pass test 1")
    else:
        print("Fail test 1")


#test 4 - check if list is empty
def emptyList(thelist):
    if not thelist:
        print("Fail test 3")
    else:
        print("Pass test 3")

#test 5 - check if searched value for borough is a string
def test_borough():
    b = isinstance(borough(), str)
    if b:
        print("Pass test 1")
    else:
        print("Fail test 1")

#test 6 - check the actual value of the searchbar
def test2_searchbar():
    assert searchbar() == "poke restaurant"

#test 7 - check the actual distance of the search
def test_dist():
    assert dist()== 500


#test 8 - check if the borough actually matches
def test_borough():
    assert borough() == "Brooklyn"
       

#test 9 - test Biz class creation
def test_Bizclass():
    p1 = Biz("Westside", "Morningside Heights", "Grocery store")
    if isinstance(p1, Biz):
        print("Pass test 9")
    else:
        print("Fail test 9")

#test 10 - test Biz class comparison
def test_Bizes():
    p1 = Biz("Westside", "Morningside Heights", "Grocery store")
    p2 = Biz("Up", "Morningside Heights", "Coffee shop")
    assert p1.location == p2.location

test_Bizes()

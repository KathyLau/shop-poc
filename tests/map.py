# example code from prof paine
def inc(x):
    """ Function that increments given integer by 1.

    Parameters
    ----------
    x : int
        The given integer.
    """

    return x + 1


# searchbar method that should only accept strings in search bar
def searchbar():
    """ Ensures seach bar only accepts strings
    """
    searchvalue = "poke restaurant"
    if isinstance(searchvalue, str):
        return searchvalue
    else:
        print("Please enter a word")


def dist():
    """ Ensures distance value is an integer
    """
    distvalue = 500
    if isinstance(distvalue, int):
        return distvalue
    else:
        print("Please enter a number")


def borough():
    """ Ensures the borough entered is a string
    """
    bvalue = "Brooklyn"
    if isinstance(bvalue, str):
        return bvalue
    else:
        print("Please enter a word")


# defining a class for list objects?
class Biz:
    """ Class that represents a buisness object

    Parameters
    ----------
    name : str
        The name of the buisiness
    location : str
        The borough where the buisiness is located
    description : str
        A description of the buisiness
    """

    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description


p1 = Biz("Westside", "Morningside Heights", "Grocery store")
p2 = Biz("Up", "Morningside Heights", "Coffee shop")

# Make a multidimensional list to store shops/businesses? a nested array?
Ls = [p1, p2]

# write a method to force certain fields to be filled? and filled with
# certain types?

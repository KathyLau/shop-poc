database package
=============

Objects
----------

SHOPS
-------------

Each shop will be stored in an SQL table following key-value pairs:

* id: integer id of data entry
* name: a string holding the shop's name
* image: link to image of shop
* text: description of shop
* service: service offered regarding takeout and delivery
* location: borough of shop
* lat: latitude address of shop
* lon: longitude address of shop
* type: type of business

==================   ============
Key                  Value
==================   ============
ID                   INT
NAME                 TEXT
IMAGE                TEXT
TEXT                 TEXT
SERVICE              TEXT
LOCATION             TEXT
LAT                  INT
LON                  INT
TYPE                 TEXT
==================   ============


SUGGESTEDSHOPS
-------------

Each suggested shop will be stored in an SQL table following key-value pairs:

* id: integer id of data entry
* name: a string holding the shop's name
* image: link to image of shop
* website: link to shop site to verify validity of shop
* service: service offered regarding takeout and delivery
* location: borough of shop
* type: type of business

==================   ============
Key                  Value
==================   ============
ID                   INT
NAME                 TEXT
IMAGE                TEXT
WEBSITE              TEXT
SERVICE              TEXT
LOCATION             TEXT
TYPE                 TEXT
==================   ============

CUSTOMERS
-------------

Each customer will be stored in an SQL table following key-value pairs:

* id: integer id of data entry
* name: a string holding the customer's name
* email: a string holding the customer's email address
* password: a string holding the customer's login password

==================   ============
Key                  Value
==================   ============
ID                   INT
NAME                 TEXT
EMAIL                TEXT
PASSWORD             TEXT
==================   ============

REVIEWS
-------------

Each customer review will be stored in an SQL table following key-value pairs:

* id: integer id of data entry
* reviewerid: integer id of customer who reviewed the shop
* shopid: integer id of shop being reviewed
* rating: an integer out of five
* review: a string holding the customer's review

==================   ============
Key                  Value
==================   ============
ID                   INT
REVIEWERID           INT
SHOPID               INT
RATING               INT
REVIEW               TEXT
==================   ============

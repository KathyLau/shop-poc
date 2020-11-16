from pymongo import MongoClient

SECRET_KEY = ""

DB_NAME = 'pocshops'

COLLECTIONS = {
    'Shop': 'shops',
    'Tag': 'tags',
    'Owner': 'owners',
    'Review': 'reviews'
}


class Model(object):

    def __init__(self, db, collection, obj=None):
        for key in obj:
            self.__dict__[key] = obj[key]
            self.db = db
            self.collection = collection
            self._obj = obj

    def get_id(self):
        return self._id

    def update_model(self):
        for key in self.__dict__:
            self._obj[key] = self.__dict__[key]

        self.collection.objects.update({'_id': self.get_id()}, self.obj)

    def remove(self):
        self.objects.remove({'_id': self._id})


class Collection(object):

    def __init__(self, model=Model):
        client = MongoClient()
        self.db = client[DB_NAME]
        self.objects = self.db[COLLECTIONS[self.__class__.__owner__]]
        self.owner = COLLECTIONS[self.__class__.__owner__]
        self.model = model

    def remove(self, **kwargs):
        self.objects.remove(kwargs)

    def remove_all(self):
        self.objects.remove()

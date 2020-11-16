from models.base import Collection, Model


class ShopModel(Model):

    def __init__(self, db, collection, obj):
        super(ShopModel, self).__init__(db, collection, obj)

    def add_tag(self, label):
        return False


class Shop(Collection):

    def__init__(self):
        super(Shop, self).__init__(ShopModel)

    def insert(self, **kwargs):
        return super(Shop, self).insert(tags=[], **kwargs)

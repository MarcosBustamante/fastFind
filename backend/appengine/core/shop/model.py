# coding: utf-8
from google.appengine.ext import ndb
from core.user.model import User

__author__ = 'bustamante'


class Shop(ndb.Model):
    image = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty(required=True)
    address = ndb.StringProperty(required=True)
    number = ndb.StringProperty(required=True)
    district = ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    latitude = ndb.FloatProperty(required=True)
    longitude = ndb.FloatProperty(required=True)

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'image': self.image,
            'name': self.name,
            'address': self.address,
            'number': self.number,
            'district': self.district,
            'city': self.city,
            'created': str(self.created),
            'updated': str(self.updated),
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    @classmethod
    def save(cls, **kwargs):
        shop = Shop()
        shop.image = kwargs.get('image')
        shop.name = kwargs['name']
        shop.address = kwargs['address']
        shop.number = kwargs['number']
        shop.district = kwargs['district']
        shop.city = kwargs['city']
        shop.latitude = kwargs['latitude']
        shop.longitude = kwargs['longitude']
        shop.put()
        return shop

    @classmethod
    def update(cls, **kwargs):
        shop = Shop.get_by_id(kwargs['id'])
        shop.image = kwargs['image']
        shop.name = kwargs['name']
        shop.address = kwargs['address']
        shop.number = kwargs['number']
        shop.district = kwargs['district']
        shop.city = kwargs['city']
        shop.put()
    
    
class RShopXUser(ndb.Model):
    user = ndb.KeyProperty(User)
    shop = ndb.KeyProperty(Shop)

    @classmethod
    def save(cls, user_key, shop_key):
        rsxu = RShopXUser(user=user_key, shop=shop_key).put()
        return rsxu

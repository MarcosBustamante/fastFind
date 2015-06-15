# coding: utf-8
from google.appengine.ext import ndb
from core.shop.model import Shop

__author__ = 'bustamante'


class Product(ndb.Model):
    images = ndb.StringProperty(repeated=True, indexed=False)
    name = ndb.StringProperty(required=True)
    price = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'images': self.images,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'created': str(self.created),
            'updated': str(self.updated)
        }

    @classmethod
    def save(cls, **kwargs):
        kwargs = _normalize(kwargs)
        product = Product()
        product.images = kwargs.get('images')
        product.name = kwargs['name']
        product.price = kwargs['price']
        product.description = kwargs['description']
        product.put()
        return product

    @classmethod
    def update(cls, **kwargs):
        product = Product.get_by_id(kwargs['id'])
        product.images = kwargs.get('images')
        product.name = kwargs['name']
        product.price = kwargs['price']
        product.description = kwargs['description']
        product.put()
        return product


class RProductXShop(ndb.Model):
    shop = ndb.KeyProperty(Shop)
    product = ndb.KeyProperty(Product)

    @classmethod
    def save(cls, product_key, shop_key):
        rpxs = RProductXShop(product=product_key, shop=shop_key).put()
        return rpxs


def _normalize(form):
    if form.get('images') is not None:
        form['images'] = [img for img in form['images'] if img]
    return form

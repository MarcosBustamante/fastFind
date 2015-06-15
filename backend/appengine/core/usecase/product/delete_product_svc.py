# coding: utf-8
from google.appengine.ext import ndb
from core.product.model import Product, RProductXShop
from core.shop.model import Shop

__author__ = 'bustamante'


def delete(shop_id, product_id):
    product = Product.get_by_id(product_id)
    shop = Shop.get_by_id(shop_id)
    query = RProductXShop.query(RProductXShop.product == product.key,
                             RProductXShop.shop == shop.key)
    rpxs = query.get()
    ndb.delete_multi([rpxs.key, product.key])

# coding: utf-8
from core.product.model import RProductXShop
from core.shop.model import RShopXUser
from google.appengine.ext import ndb

__author__ = 'bustamante'


def listing(user):
    query = RShopXUser.query(user.key == RShopXUser.user)
    shop_keys = [q.shop for q in query]

    product_keys = []
    map_product_id_x_shop_id = {}
    for shop_key in shop_keys:
        query = RProductXShop.query(RProductXShop.shop == shop_key)
        for q in query:
            product_keys.append(q.product)
            map_product_id_x_shop_id[q.product.id()] = shop_key.id()

    products = ndb.get_multi(product_keys)

    products_dict_json = []
    for p in products:
        to_dict = p.to_dict_json()
        to_dict['store'] = map_product_id_x_shop_id[to_dict['id']]
        products_dict_json.append(to_dict)

    return products_dict_json

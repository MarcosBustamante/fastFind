# coding: utf-8
from core.shop.model import RShopXUser
from google.appengine.ext import ndb

__author__ = 'bustamante'


def listing(user):
    query = RShopXUser.query(user.key == RShopXUser.user)
    shop_keys = [q.shop for q in query]
    shops = ndb.get_multi(shop_keys)
    shop_dict_json = [s.to_dict_json() for s in shops]
    return shop_dict_json

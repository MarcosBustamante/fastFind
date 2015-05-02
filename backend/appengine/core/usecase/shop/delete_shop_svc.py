# coding: utf-8
from core.shop.model import RShopXUser, Shop
from google.appengine.ext import ndb

__author__ = 'bustamante'


def delete(user, shop_id):
    shop = Shop.get_by_id(shop_id)
    query = RShopXUser.query(user.key == RShopXUser.user,
                             RShopXUser.shop == shop.key)
    rsxu = query.get()
    ndb.delete_multi([rsxu.key])

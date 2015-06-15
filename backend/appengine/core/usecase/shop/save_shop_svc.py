# coding: utf-8
from core.shop.model import Shop, RShopXUser
from core.user.model import User, USER, SHOP

__author__ = 'bustamante'


def save(user, form):
    _validate_form(form)
    if 'id' in form:
        shop = Shop.update(**form)
    else:
        shop = Shop.save(**form)
        RShopXUser.save(user.key, shop.key)
    return shop.to_dict_json()


def _validate_form(form):
    errors = []

    if form.get('name') is None:
        errors.append('name')
    if form.get('address') is None:
        errors.append('address')
    if form.get('number') is None:
        errors.append('number')
    if form.get('district') is None:
        errors.append('district')
    if form.get('city') is None:
        errors.append('city')
    if form.get('latitude') is None:
        errors.append('latitude')
    if form.get('longitude') is None:
        errors.append('longitude')

    if len(errors) > 0:
        raise Exception(u'Parametros sao necessarios %s' % errors)
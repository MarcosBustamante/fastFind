# coding: utf-8
from core.product.model import Product, RProductXShop
from core.shop.model import Shop

__author__ = 'bustamante'


def save(form):
    _validate_form(form)
    shop_key = Shop.get_by_id(form['store'])

    if shop_key is None:
        raise Exception('A loja não existe :(')

    shop_key = shop_key.key
    if 'id' in form:
        product = Product.update(**form)
    else:
        product = Product.save(**form)
        RProductXShop.save(product.key, shop_key)
    return product.to_dict_json()


def _validate_form(form):
    errors = []

    if form.get('name') is None:
        errors.append('name')
    if form.get('store') is None:
        errors.append('store')
    if form.get('price') is None:
        errors.append('price')
    if form.get('description') is None:
        errors.append('description')

    if len(errors) > 0:
        raise Exception(u'Parametros sao necessarios %s' % errors)

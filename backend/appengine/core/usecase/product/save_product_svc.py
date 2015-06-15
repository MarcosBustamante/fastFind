# coding: utf-8
from core.product.model import Product, RProductXShop
from core.shop.model import Shop

__author__ = 'bustamante'


def save(form):
    _validate_form(form)
    shop_key = Shop.get_by_id(form['store']).key

    if shop_key is None:
        Exception('A loja não existe :(')

    if 'id' in form:
        Product.update(**form)
        product_dictj = {}
    else:
        product = Product.save(**form)
        RProductXShop.save(product.key, shop_key)
        product_dictj = product.to_dict_json()

    return product_dictj


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

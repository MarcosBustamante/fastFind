# coding: utf-8
from core.user.model import User

__author__ = 'bustamante'


def save(**form):
    if 'id' in form:
        user = User.update(**form)
    else:
        user = User.save(**form)
    return user.to_dict_json()
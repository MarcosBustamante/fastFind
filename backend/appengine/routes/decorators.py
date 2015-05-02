# coding: utf-8
import functools
from core.user.model import User
from gaecookie import facade
MY_USER_COOKIE_NAME = 'myLoggedUser'
__author__ = 'bustamante'


def get_logged_user(_req,):
    result = facade.retrive_cookie_data(_req, MY_USER_COOKIE_NAME).execute().result
    if result is None:
        return None
    user_id = result.get('id')
    return User.get_by_id(user_id)

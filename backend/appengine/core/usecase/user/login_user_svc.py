# coding: utf-8
from core.user.model import User
from gaecookie import facade

__author__ = 'bustamante'


def logar(resp, pw, login):
    user = User.find_by_login(login)

    if user is None or user.password != pw:
        raise Exception('Login ou senha invalida')

    facade.write_cookie(resp, 'myLoggedUser', {'id': user.key.id()}).execute()
    return user.to_dict_json()


def logout(_resp):
    facade.delete_cookie(_resp, 'myLoggedUser').execute()

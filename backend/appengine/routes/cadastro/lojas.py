# coding: utf-8
from __future__ import absolute_import, unicode_literals
import json
from config.template_middleware import TemplateResponse
from core.usecase.shop import save_shop_svc, list_shop_svc, delete_shop_svc
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.decorators import get_logged_user
from tekton.router import to_path
from routes.login.home import index as login_index


@login_not_required
@no_csrf
def index(_handler, _req):
    user = get_logged_user(_req)
    if user is None:
        _handler.redirect(to_path(login_index))
    else:
        value = {
            'user': json.dumps(user.to_dict_json())
        }
        return TemplateResponse(context=value)


@login_not_required
@no_csrf
def salvar(_handler, _req, _resp, form):
    user = get_logged_user(_req)
    to_dict = json.loads(form)

    if user is None:
        _handler.redirect(to_path(login_index))
    else:
        result = save_shop_svc.save(user, to_dict)
        _resp.write(json.dumps(result))


@login_not_required
@no_csrf
def listar(_handler, _req, _resp):
    user = get_logged_user(_req)

    if user is None:
        _handler.redirect(to_path(login_index))
    else:
        result = list_shop_svc.listing(user)
        _resp.write(json.dumps(result))


@login_not_required
@no_csrf
def deletar(_handler, _req, **kwargs):
    user = get_logged_user(_req)

    if user is None:
        _handler.redirect(to_path(login_index))
    else:
        delete_shop_svc.delete(user, kwargs['id'])

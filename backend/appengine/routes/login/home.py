# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from core.usecase.user import login_user_svc
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from routes.decorators import get_logged_user
from tekton.router import to_path
from routes.home import index as home_index


@login_not_required
@no_csrf
def index(_req):
    user = get_logged_user(_req)
    userj = {} if user is None else user.to_dict_json()
    value = {
        'user': json.dumps(userj)
    }
    return TemplateResponse(context=value)


@login_not_required
@no_csrf
def sing_in(_resp, password, login):
    result = login_user_svc.logar(_resp, password, login)
    _resp.write(json.dumps(result))


@login_not_required
@no_csrf
def sing_out(_resp, _handler):
    login_user_svc.logout(_resp)
    _handler.redirect(to_path(home_index))

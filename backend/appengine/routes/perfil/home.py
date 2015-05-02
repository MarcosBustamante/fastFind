# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from routes.decorators import get_logged_user
from core.usecase.user import save_user_svc

__author__ = 'bustamante'


@login_not_required
@no_csrf
def index(_req):
    value = {
        'user': get_logged_user(_req).to_dict_json()
    }
    return TemplateResponse(context=value)


@login_not_required
@no_csrf
def save(_req, _resp, **kwargs):
    save_user_svc.save(**kwargs)
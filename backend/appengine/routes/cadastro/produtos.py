# coding: utf-8
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.decorators import get_logged_user
from routes.login.home import index as login_index
import json


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

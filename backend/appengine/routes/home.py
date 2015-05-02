# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.decorators import get_logged_user
import json


@login_not_required
@no_csrf
def index(_req):
    user = get_logged_user(_req)
    user_dict = {} if user is None else user.to_dict_json()
    value = {
        'user': json.dumps(user_dict)
    }
    return TemplateResponse(context=value)

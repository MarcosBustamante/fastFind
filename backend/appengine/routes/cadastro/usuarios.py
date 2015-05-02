# coding: utf-8
from __future__ import absolute_import, unicode_literals
import json
from core.usecase.user import save_user_svc
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required

__author__ = 'bustamante'


@login_not_required
@no_csrf
def salvar(_resp, form):
    to_dict_form = json.loads(form)
    result = save_user_svc.save(**to_dict_form)
    _resp.write(json.dumps(result))

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from google.appengine.api import images
from gaepermission.decorator import login_not_required
import json

__author__ = 'bustamante'

@login_not_required
@no_csrf
def index(_handler, _resp):
    blob_infos = _handler.get_uploads("file")
    _resp.write(json.dumps({'link': images.get_serving_url(blob_infos[0].kek)}))

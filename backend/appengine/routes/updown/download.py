# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required

__author__ = 'bustamante'


@no_csrf
@login_required
def index(_handler, blob_key, filename):
    _handler.send_blob(blob_key)

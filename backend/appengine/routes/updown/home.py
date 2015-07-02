# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
import json
from google.appengine.api.app_identity import get_default_gcs_bucket_name
from google.appengine.ext.blobstore import blobstore
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
# from routes.updown import upload
from tekton import router
from gaepermission.decorator import login_not_required

import re
import webapp2
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore

__author__ = 'marcos'


@no_csrf
@login_not_required
def index(_resp):
    success_url = router.to_path(upload)
    bucket = get_default_gcs_bucket_name()
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    _resp.write(json.dumps({'upload_url': url}))



@login_not_required
@no_csrf
def upload(_handler, _resp):
    blob_infos = _handler.get_uploads("file")
    _resp.write(json.dumps({'link': images.get_serving_url(blob_infos[0].kek)}))

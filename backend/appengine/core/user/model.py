# coding: utf-8
__author__ = 'bustamante'
from google.appengine.ext import ndb
from datetime import datetime

SHOP = 'SHOP'
USER = 'USER'
ADMIN = 'ADMIN'


class User(ndb.Model):
    login = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=False)
    name = ndb.StringProperty(required=False, default='')
    email = ndb.StringProperty(required=True)
    birth = ndb.DateProperty(required=False)
    avatar = ndb.BlobKeyProperty(required=False)
    permissions = ndb.StringProperty(choices=['SHOP', 'USER', 'ADMIN'], repeated=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    def to_dict_json(self):
        return {
            'id': str(self.key.id()),
            'login': self.login.encode('utf-8'),
            'name': self.name.encode('utf-8'),
            'email': self.email.encode('utf-8'),
            'birth': str(self.birth),
            'avatar': self._get_avatar().encode('utf-8'),
            'permissions': self.permissions,
            'created': str(self.created),
            'updated': str(self.updated),
        }

    @classmethod
    def save(cls, **form):
        if cls.find_by_login(form['login']) is not None:
            raise Exception('Login already exist')

        user = User()
        user.login = form['login'].lower()
        user.password = form['password']
        user.email = form['email']
        user.put()
        return user

    @classmethod
    def update(cls, **form):
        user = User.query(User.login == form['login']).get()
        user.name = form['name']
        if form['birth'] is not None or form['birth'] != 'None':
            user.birth = datetime.strptime(form['birth'], '%Y-%m-%d').date()
        user.email = form['email']
        user.put()
        return user

    @classmethod
    def find_by_login(cls, login):
        return User.query(User.login == login.lower()).get()

    def _get_avatar(self):
        if self.avatar == None or self.avatar == '':
            return '/static/img/user.png'
        return self.avatar
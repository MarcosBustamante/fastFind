# coding: utf-8
from copy import deepcopy
from base import GAETestCase
from core.usecase.shop import save_shop_svc
from core.user.model import User
from mommygae import mommy

__author__ = 'bustamante'


class ShopSaveTests(GAETestCase):
    def setUp(self):
        super(ShopSaveTests, self).setUp()
        self.user = mommy.make_one(User, login='testando',
                                   password='123456',
                                   email='teste@gmail.com',
                                   permissions=('USER',))
        self.form = {
            'name': 'meu nome',
            'address': 'meu address',
            'number': '123456',
            'district': 'meu district',
            'city': 'minha city',
            'latitude': 12334,
            'longitude': 123456
        }

    def test_save_with_success(self):
        shop_dict_save = save_shop_svc.save(self.user, self.form)

        self.assertIsInstance(shop_dict_save, dict)
        self.assertIsNotNone(shop_dict_save['id'])
        self.assertEquals(shop_dict_save['name'], self.form['name'])

        form_upddate = deepcopy(shop_dict_save)
        form_upddate['name'] = 'meu nome update'

        shop_dict_update = save_shop_svc.save(self.user, form_upddate)

        self.assertIsInstance(shop_dict_update, dict)
        self.assertIsNotNone(shop_dict_update['id'])
        self.assertEquals(shop_dict_update['id'], shop_dict_save['id'])
        self.assertEquals(shop_dict_update['name'], form_upddate['name'])
        self.assertNotEquals(shop_dict_update['name'], shop_dict_save['name'])

    def test_save_without_success(self):
        with self.assertRaises(Exception) as vt:
            save_shop_svc.save(self.user, {'name': 'meu nome'})

        self.assertIn('address', vt.exception.message)
        self.assertIn('number', vt.exception.message)
        self.assertIn('district', vt.exception.message)
        self.assertIn('city', vt.exception.message)
        self.assertIn('latitude', vt.exception.message)
        self.assertIn('longitude', vt.exception.message)

# coding: utf-8
from copy import deepcopy
from base import GAETestCase
from core.product.model import RProductXShop
from core.shop.model import Shop
from core.usecase.product import save_product_svc
from core.user.model import User
from mommygae import mommy

__author__ = 'bustamante'


class ProductSaveTests(GAETestCase):
    def setUp(self):
        super(ProductSaveTests, self).setUp()
        self.shop = mommy.make_one(Shop, name='meu nome',
                                   address='meu address',
                                   number='123456',
                                   district='meu district',
                                   city='minha city',
                                   latitude=12334,
                                   longitude=123456).put().get()
        self.product = {
            'images': [],
            'name': 'meu produto',
            'price': 'R$ 2.000.000,00',
            'description': 'minha description',
            'store': self.shop.key.id()
        }

    def test_save_with_success(self):
        shop_dict_save = save_product_svc.save(self.product)
        rpxs = RProductXShop.query(RProductXShop.shop == Shop.get_by_id(self.product['store']).key).get()

        self.assertTrue(shop_dict_save)
        self.assertEquals(shop_dict_save['name'], 'meu produto')
        self.assertTrue(rpxs)

    def test_save_without_success(self):
        with self.assertRaises(Exception) as vt:
            save_product_svc.save({})

        self.assertIn('name', vt.exception.message)
        self.assertIn('description', vt.exception.message)
        self.assertIn('price', vt.exception.message)
        self.assertIn('store', vt.exception.message)

        self.product['store'] = 12345

        with self.assertRaises(Exception) as vt:
            save_product_svc.save(self.product)

        self.assertEquals(vt.exception.message, 'A loja não existe :(')

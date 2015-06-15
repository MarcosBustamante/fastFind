# coding: utf-8
from base import GAETestCase
from core.shop.model import Shop, RShopXUser
from core.usecase.shop import delete_shop_svc, list_shop_svc
from core.user.model import User
from mommygae import mommy

__author__ = 'bustamante'


class ShopDeleteTests(GAETestCase):
    def setUp(self):
        super(ShopDeleteTests, self).setUp()
        self.user = mommy.make_one(User, login='testando',
                                   password='123456',
                                   email='teste@gmail.com',
                                   permissions=('USER',)).put().get()
        self.shop = mommy.make_one(Shop, name='meu nome',
                                   address='meu address',
                                   number='123456',
                                   district='meu district',
                                   city='minha city',
                                   latitude=12334,
                                   longitude=123456).put().get()
        self.rsxu = mommy.make_one(RShopXUser, shop=self.shop.key,
                                   user=self.user.key).put().get()

    def test_delete(self):
        shops = list_shop_svc.listing(self.user)

        self.assertTrue(shops)
        self.assertEquals(len(shops), 1)
        self.assertEquals(shops[0]['name'], 'meu nome')

        delete_shop_svc.delete(self.user, self.shop.key.id())

        shops = list_shop_svc.listing(self.user)

        self.assertFalse(shops)
        self.assertEquals(len(shops), 0)

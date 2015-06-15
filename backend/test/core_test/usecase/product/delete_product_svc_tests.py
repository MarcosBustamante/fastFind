# coding: utf-8
from base import GAETestCase
from core.product.model import Product, RProductXShop
from core.shop.model import Shop, RShopXUser
from core.usecase.product import list_product_svc, delete_product_svc
from core.user.model import User
from mommygae import mommy

__author__ = 'bustamante'


class ProductDeleteTests(GAETestCase):
    def setUp(self):
        super(ProductDeleteTests, self).setUp()
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

        self.product = mommy.make_one(Product,
                                      images=[],
                                      name='meu produto',
                                      price='R$ 2.000.000,00',
                                      description='minha description').put().get()

        self.rsxu = mommy.make_one(RShopXUser, shop=self.shop.key,
                                   user=self.user.key).put().get()

        self.rpxs = mommy.make_one(RProductXShop, shop=self.shop.key,
                                   product=self.product.key).put().get()

    def test_delete(self):
        products = list_product_svc.listing(self.user)

        self.assertTrue(products)
        self.assertEquals(len(products), 1)
        self.assertEquals(products[0]['name'], 'meu produto')

        delete_product_svc.delete(self.shop.key.id(), self.product.key.id())

        products = list_product_svc.listing(self.user)

        self.assertFalse(products)
        self.assertEquals(len(products), 0)

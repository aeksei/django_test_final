from django.test import TestCase

from ..models import User, Product, Cart
#
#
# class TestUser(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         User.objects.create(email='test@gmail.com',
#                             first_name='first_name',
#                             last_name='last_name',
#                             age=10)
#
#     def test_initial(self):
#         user = User.objects.get(pk=1)
#
#         self.assertEqual(user.email, 'test@gmail.com')
#         self.assertEqual(user.first_name, 'first_name')
#
#     def test_str(self):
#         user = User.objects.get(pk=1)
#         self.assertEqual(str(user), 'test@gmail.com')
#
#
# class TestProduct(TestCase):
#     def setUp(self) -> None:
#         Product.objects.create(name='banana', price=120, discount=30, discount_price=100, type='fruits')
#
#     def test_str(self):
#         prod = Product.objects.get(name='banana')
#         self.assertEqual(str(prod), 'banana')
#
#
#     def test_discount_str(self):
#         prod = Product.objects.get(name='banana')
#         self.assertEqual(prod.discount_str(), '30%')
#         self.assertEqual(len(Product.objects.all()), 1)


class TestCart(TestCase):
    def test_str(self):
        user = User.object.create()
        product = Product.objects.create()

        Cart.objects.create(user=user, product=product, count=1)
        cart = Cart.objects.get(pk=1)
        self.assertEqual(str(cart), "1 - User... - Product ...")

    def test_unique_together(self):
        self.assertEqual(Cart.Meta.unique_together,
                         (('user', 'product'), ))




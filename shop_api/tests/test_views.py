from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.test.utils import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Product


class TestProduct(APITestCase):
    def setUp(self) -> None:
        Product.objects.create(
            name='test',
            price=100,
            discount_price=50,
            discount=50,
            type='fruits'
        )

    def test_list(self):
        Product.objects.create(
            name='test2',
            price=200,
            discount_price=50,
            discount=100,
            type='vegetables'
        )
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve(self):
        # /products/1
        ...

    def test_delete(self):
        response = self.client.delete('/products/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/products/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        with self.assertRaises(ObjectDoesNotExist, msg='Объект не удалился из базы'):
            Product.objects.get(pk=1)


class TestCouponViewSet(APITestCase):
    def test_not_allowed_method(self):
        not_allowed_methods = {
            'POST': self.client.post,
            'PUT': self.client.put,
            'PATCH': self.client.patch,
            'DELETE': self.client.delete
        }

        url = '/coupons/'
        for method_name, method in not_allowed_methods.items():
            response = method(url)
            self.assertEqual(
                response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED,
                msg=f"Method {method_name} should be not allowed for url: {url}")


#
#
# class TestUserViewSet(TestCase):
#     @override_settings(DEBUG=False)
#     def test_list(self):
#         print("#########")
#         User.objects.create(email='test@gmail.com',
#                             first_name='first_name',
#                             last_name='last_name',
#                             age=10)
#         url = '/users/'
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#
#
#     def test_retvireve(self):
#         User.objects.create(email='test@gmail.com',
#                             first_name='first_name',
#                             last_name='last_name',
#                             age=10)
#
#         url = '/users/1'
#         response = self.client.get(url, follow=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         url = '/users/234'
#         response = self.client.get(url, follow=True)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

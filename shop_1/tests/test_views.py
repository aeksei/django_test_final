from django.shortcuts import reverse
from django.test import TestCase
from django.test.utils import override_settings
from rest_framework import status


class TestShopView(TestCase):
    @override_settings(DEBUG=False)
    def test_get(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @override_settings(DEBUG=False)
    def test_get_reverse(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_used_template(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'shop_1/shop.html')


class TestIndexView(TestCase):
    @override_settings(DEBUG=False)
    def test_get(self):
        response = self.client.get('',  follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

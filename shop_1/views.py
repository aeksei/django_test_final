from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage

from .settings.info import INFO

# Create your views here.

class IndexView(View):

    def get(self, request):

        contex = {}
        contex.update(INFO)
        return render(request, 'shop_1/index.html', contex)


class ShopView(View):
    def get(self, request, page=1):
        products_list = [
            {
                'name': 'Bell Pepper',
                'image': 'shop_1/images/product-1.jpg',
                'price': '$150.00',
                'discount': '30%',
                'price_sale': '$100.00'
            },
            {
                'name': 'Strawberry',
                'image': 'shop_1/images/product-2.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Green Beans',
                'image': 'shop_1/images/product-3.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Purple Cabbage',
                'image': 'shop_1/images/product-4.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Tomatoe',
                'image': 'shop_1/images/product-5.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Brocolli',
                'image': 'shop_1/images/product-6.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Carrots',
                'image': 'shop_1/images/product-7.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Fruit Juice',
                'image': 'shop_1/images/product-8.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Onion',
                'image': 'shop_1/images/product-9.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Apple',
                'image': 'shop_1/images/product-10.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Garlic',
                'image': 'shop_1/images/product-11.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Chilli',
                'image': 'shop_1/images/product-12.jpg',
                'price': '$120.00'
            }
        ]

        product_on_page = 2
        paginator = Paginator(products_list, product_on_page)


        # products_list = paginator.page(page)
        try:
            products_list = paginator.page(page)
            products_list.page_tuple = tuple(paginator.page_range)
        except EmptyPage:
            return redirect(reverse('shop'))

        contex = {'page_obj': products_list}
        contex.update(INFO)
        return render(request, 'shop_1/shop.html', contex)

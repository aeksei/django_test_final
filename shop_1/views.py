from django.shortcuts import render
from django.views import View

from .settings.info import INFO

# Create your views here.

class IndexView(View):

    def get(self, request):

        contex = {}
        contex.update(INFO)
        return render(request, 'shop_1/index.html', contex)


class ShopView(View):

    def get(self, request):
        contex = {}
        contex.update(INFO)
        return render(request, 'shop_1/shop.html', contex)

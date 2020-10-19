from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Product, Cart

# Create your views here.


class ProductView(View):

    def get(self, request):
        product = Product.objects.all()
        if 'type' in request.GET:
            product = product.filter(type=request.GET['type'])
        print(product)
        return HttpResponse(product)

    def post(self, request):
        params = request.POST
        product = Product(name=params['name'])
        try:
            product.save()
        except Exception as e:
            return HttpResponse(f"Product create error !")

        return HttpResponse(f"Product {list(params.items())} create successful!")


class CartView(View):
    def get(self, request):
        email = request.GET['email']
        cart = Cart.objects.filter(user__email=email).order_by('-create_at')

        return HttpResponse(cart)








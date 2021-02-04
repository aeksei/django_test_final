from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Product, Cart

# Create your views here.


class ProductView(LoginRequiredMixin, View):
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



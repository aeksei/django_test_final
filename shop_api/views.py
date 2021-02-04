from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import User, Product, Coupon, Cart
from .serializers import UserSerializer, ProductSerializer, CouponSerializer, CartSerializer
from .filters import ProductFilter, CartFilter
from shop_1.views import ShopView
# Create your views here.


class UserViewSet(ModelViewSet):
    """
    list: Список пользователей

    create: Создание нового пользователя

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filterset_class = ProductFilter

    # def list(self, request, *args, **kwargs):
    #     filter_params = {param: request.GET[param] for param in request.GET}
    #
    #     queryset = self.get_queryset()
    #     filter_queryset = queryset.filter(**filter_params)
    #
    #     serializer = self.get_serializer(filter_queryset, many=True)
    #
    #     return Response(serializer.data)


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    lookup_field = 'name'


class CartViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    """
    API для корзины

    list:
    API для получения списка корзины

    add:
    Добавление продукта конкретному пользователю в корзину
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    filterset_class = CartFilter

    @action(methods=['GET'], detail=False)
    def add(self, request):
        print(request.user)
        product = request.GET['product']
        user = request.GET['user']
        count = request.GET['count']

        serializer = self.get_serializer(data=dict(user=user, product=product, count=count))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

    @action(methods=['GET'], detail=False)
    def delete(self, request):
        product = request.GET['product']
        user = request.GET['user']

        self.get_queryset().get(user__id=user, product__id=product).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

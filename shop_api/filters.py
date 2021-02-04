from django_filters import rest_framework as filters
from .models import Product, Cart


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name',
                              lookup_expr='exact',
                              help_text='Название продукта')

    discount = filters.NumberFilter(field_name='discount',
                                    help_text='Скидка')

    price_min = filters.NumberFilter(field_name='price',
                                     lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='price',
                                     lookup_expr='lte')

    class Meta:
        model = Product
        fields = (
            'name',
            'discount',
            'price_min',
            'price_max',
        )


class CartFilter(filters.FilterSet):
    count = filters.NumberFilter(field_name='count',
                                 help_text='Количетво товара')

    discount_product = filters.NumberFilter(field_name='product__discount',
                                            lookup_expr='gte',
                                            help_text='Товар со скидкой не меньше, чем ...')

    # type = filters.ChoiceFilter(choices=Product.TYPE)
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    # name = filters.CharFilter(field_name='name', lookup_expr='exact')
    #
    class Meta:
        model = Cart
        fields = [
            'count',
            'discount_product',
        ]

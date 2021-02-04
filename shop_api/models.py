from django.db import models
import jsonfield
from django.contrib.auth.models import User as UserAuth


# Create your models here.


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    # from django.contrib.auth.models import User as UserAuth
    auth_user = models.OneToOneField(UserAuth, null=True, on_delete=models.SET_NULL)

    age = models.IntegerField()

    def __str__(self):
        return f'{self.email}'


class Product(models.Model):
    TYPE = (
        ('fruits', 'fruits'),
        ('vegetables', 'vegetables'),
    )

    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField()
    discount = models.IntegerField()

    type = models.CharField(max_length=10, choices=TYPE)

    def discount_str(self):
        return f'{self.discount}%'

    def __str__(self):
        return f'{self.name}'

    @property
    def total_price(self):
        return self.price * (1 - self.discount * 0.01)


class Coupon(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    value = models.IntegerField()
    min_coast = models.IntegerField()
    start_at = models.DateField()
    finish_at = models.DateField()


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = (('user', 'product'), )

    def __str__(self):
        return f'{self.id}-{self.user}-{self.product}'


class JsonModel(models.Model):
    the_json = jsonfield.JSONField()

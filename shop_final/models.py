from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    year = models.PositiveSmallIntegerField()
    pages = models.PositiveSmallIntegerField()
    isbn13 = models.CharField(max_length=13)  # todo isbn validate
    rating = models.PositiveSmallIntegerField()
    price = models.FloatField()  # todo need above zero
    discount = models.PositiveSmallIntegerField(null=True)

    def price_sale(self):
        return self.discount or self.price * self.discount * 0.01



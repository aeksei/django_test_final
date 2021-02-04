from django.contrib import admin
from .models import User, Product, Cart, JsonModel


# Register your models here.
class CartAdminInline(admin.StackedInline):
    model = Cart

    extra = 0

    max_num = 3

#
#
# class UserAdminInline(admin.TabularInline):
#     model = User
#
#

class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'first_name', 'last_name')
    fields = ('email', ('first_name', 'last_name'), 'age')

    inlines = (CartAdminInline, )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'discount_str')
    # list_display_links = ('discount_str', )

    ordering = ('-discount', )



admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(JsonModel)

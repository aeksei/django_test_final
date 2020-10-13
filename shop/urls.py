from django.urls import path

from .views import ProductViewAdd, ProductView


urlpatterns = [
    path('product/add', ProductViewAdd.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
]

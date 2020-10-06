from django.urls import path
from .views import *

urlpatterns = [
    path('blogs_view/', get_blogs_view),
    path('blogs_view/<int:year>', get_blog_year_view),
    path('blogs_view/<int:year>/<int:pk>', get_article, name="article"),
]

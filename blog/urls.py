import json

from django.urls import path, re_path
from django.http import HttpResponse, JsonResponse

blogs = {
    2019: [
        {
            'author': 'Пушкин',
            'date': '03.06.2019',
            'like': 20
        },
        {
            'author': 'Толстой',
            'date': '27.07.2019',
            'like': 100
        }
    ],
    2020: [
        {
            'author': 'Лермонтов',
            'date': '07.10.2020',
            'like': 73
        }
    ],
}


def _get_blogs_view(request):
    html = ""
    for year in blogs:
        html += f"{year}<br>"

    return HttpResponse(html)


def _get_blog_year_view(request, year):
    d = {}
    for i, value in enumerate(blogs[int(year)]):
        d[i] = value
    return JsonResponse(d)


def _get_article(request, year, pk):
    try:
        return JsonResponse(blogs[year][pk])
    except IndexError:
        return HttpResponse("<h1>Такой статьи нет</h1>")


urlpatterns = [
    path('blogs_view/', _get_blogs_view),
    path('blogs_view/<int:year>', _get_blog_year_view),
    path('blogs_view/<int:year>/<int:pk>', _get_article),
]

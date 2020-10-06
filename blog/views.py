from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse

# Create your views here.

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


def get_blogs_view(request):
    # todo url redirect
    html = ""
    for year in blogs:
        html += f"{year}<br>"

    return HttpResponse(html)


def get_blog_year_view(request, year):
    url = reverse('article', args=(year, 0))
    return redirect(url)


def get_article(request, year, pk=None):
    try:
        return JsonResponse(blogs[year][pk])
    except IndexError:
        return HttpResponse("<h1>Такой статьи нет</h1>")

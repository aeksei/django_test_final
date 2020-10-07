from django.shortcuts import render
from django.views import View


def index(request):
    """Функцональный подход для View"""
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        return render(request, 'index.html')


class IndexView(View):
    """Классовый подход для View"""
    def get(self, request):
        return render(request, 'index.html')

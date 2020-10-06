import sys
from datetime import datetime

from django.urls import path
from django.http import HttpResponse, JsonResponse

from .views import IndexView


def _get_info(request):
    # html = f"""<html><body>{sys.platform} | {sys.version}</body></html>"""
    json_ = {
        'platform': sys.platform,
        'python': sys.version
    }

    return JsonResponse(json_)


def _get_date(request):
    html = f"""{datetime.now()}"""
    return HttpResponse(html)


urlpatterns = [
    path('', IndexView.as_view()),
    path('info/', _get_info),
    path('date/', _get_date),
]

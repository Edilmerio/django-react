from django.urls import re_path

from .api_rest import ListEdificios

urlpatterns = [
    re_path(r'^edificios/$', ListEdificios.as_view(), name="list_edificios")
]
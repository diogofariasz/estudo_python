from django.urls import path
from mainpage.views import *

urlpatterns = [
    path('main/', main_view, name='main'),
    path('noticia01/', noticia01_view, name='noticia01'),
    path('noticia02/', noticia02_view, name='noticia02'),
]
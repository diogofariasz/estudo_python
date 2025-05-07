from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'main.html')

def noticia01_view(request):
    return render(request, 'noticia01.html')

def noticia02_view(request):
    return render(request, 'noticia02.html')
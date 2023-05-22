from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def index(request):
    return render(request, template_name='galeria/index.html')

def imagem(request):
    return render(request, template_name='galeria/imagem.html')
from django.shortcuts import render

def index(request):
    return render(request, template_name='galeria/index.html')

def imagem(request):
    return render(request, template_name='galeria/imagem.html')
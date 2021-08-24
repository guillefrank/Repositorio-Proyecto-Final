from django.shortcuts import render
# Create your views here.

def listar_preguntas(request):
    return render(request, 'juego/listar_preguntas.html', {})
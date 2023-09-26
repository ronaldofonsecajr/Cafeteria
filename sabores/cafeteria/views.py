from django.shortcuts import render
from .models import Usuario

def home(request):
    return render (request,'cafe/home.html')

def pedidos(resquest):
    novo_usuario = Usuario()
    novo_usuario.nome = resquest.POST.get('nome')
    novo_usuario.email = resquest.POST.get('email')
    novo_usuario.celular = resquest.POST.get('celular')
    novo_usuario.endereco = resquest.POST.get('endereco')
    novo_usuario.combo = resquest.POST.get('combo')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(resquest,'cafe/pedidos.html',usuarios)
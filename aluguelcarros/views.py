from django.shortcuts import render, get_object_or_404, redirect
from .models import Carro, Cliente, Reserva
from .forms import CarroForm, ClienteForm, ReservaForm

def home(request):
    return render(request, 'home.html')


def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'listar_carros.html', {'carros': carros})

def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, 'detalhes_carro.html', {'carro': carro})

def adicionar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm()
    return render(request, 'adicionar_carro.html', {'form': form})

def editar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'editar_carro.html', {'form': form, 'carro': carro})

def excluir_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    carro.delete()
    return redirect('listar_carros')
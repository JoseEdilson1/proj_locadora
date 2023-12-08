from django import forms
from .models import Carro, Cliente, Reserva

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=20, unique=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    preco_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Reserva de {self.carro} para {self.cliente} de {self.data_retirada} a {self.data_devolucao}"
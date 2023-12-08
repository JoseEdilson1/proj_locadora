from django.urls import path
from . import views

app_name = 'aluguelcarros'  # Substitua 'seu_app_nome' pelo nome real do seu aplicativo

urlpatterns = [
    path('carros/', views.listar_carros, name='listar_carros'),
    path('carro/<int:carro_id>/', views.detalhes_carro, name='detalhes_carro'),
    path('carro/adicionar/', views.adicionar_carro, name='adicionar_carro'),
    path('carro/editar/<int:carro_id>/', views.editar_carro, name='editar_carro'),
    path('carro/excluir/<int:carro_id>/', views.excluir_carro, name='excluir_carro'),
    # Adicione mais URLs para Cliente e Reserva, se necessário
]

from django.contrib import admin
from django.urls import include, path
from aluguelcarros.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluguelcarros/', include('aluguelcarros.urls')),
    # Adicione mais paths para outros aplicativos, se necessário
    path('', home, name='home'),
]

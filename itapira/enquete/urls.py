# importando a função path
from django.urls import path
# enxergando o arquivo de views
from . import views
# 
urlpatterns = [
    path('', views.index, name='index'),
    path('loucura', views.loucura, name='loucura'),
]
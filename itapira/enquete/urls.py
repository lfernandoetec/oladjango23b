# importando a função path
from django.urls import path
# enxergando o arquivo de views
from . import views
# 
urlpatterns = [
    path('', views.index, name='index'),
    path('loucura', views.loucura, name='loucura'),
    # ex: /enquete/5/
    path("<int:questao_id>/", views.detalhe, name="detalhe"),
    # ex: /enquete/5/resultados/
    path("<int:questao_id>/resultados/", views.resultados, name="resultados"),
    # ex: /enquete/5/voto/
    path("<int:questao_id>/voto/", views.voto, name="voto"),
]
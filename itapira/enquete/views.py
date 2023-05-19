from django.shortcuts import render
from django.http import HttpResponse
from .models import Questao

# Create your views here.
def index(request):
    ultimas_questoes = Questao.objects.order_by("-data")[:5]
    saida = ", ".join([q.pergunta for q in ultimas_questoes])
    return HttpResponse(saida)

def loucura(request):
    return HttpResponse("E nessa loucura.......")

def detalhe(request, questao_id):
    return HttpResponse("Voce esta olhando a questao %s." % questao_id)


def resultados(request, questao_id):
    response = "Voce esta olhando o resultado da questao %s."
    return HttpResponse(response % questao_id)


def voto(request, questao_id):
    return HttpResponse("Voce esta votando na questao %s." % questao_id)
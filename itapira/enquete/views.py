from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Questao

# Create your views here.
def index(request):
    ultimas_questoes = Questao.objects.order_by("-data")[:5]
    context = {'ultimas_questoes': ultimas_questoes}
    return render(request, 'enquete/index.html', context)

def loucura(request):
    return HttpResponse("E nessa loucura.......")

def detalhe(request, questao_id):
    try:
        questao = Questao.objects.get(pk=questao_id)
    except Questao.DoesNotExist:
        raise Http404("Questao naum ecxisty")
    return render(request, 'enquete/questao.html', {'questao': questao})


def resultados(request, questao_id):
    response = "Voce esta olhando o resultado da questao %s."
    return HttpResponse(response % questao_id)


def voto(request, questao_id):
    return HttpResponse("Voce esta votando na questao %s." % questao_id)
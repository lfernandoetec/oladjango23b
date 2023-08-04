from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Questao, Resposta

# Create your views here.
def index(request):
    ultimas_questoes = Questao.objects.order_by("-data")#[:5]
    context = {'ultimas_questoes': ultimas_questoes}
    return render(request, 'enquete/index.html', context)

def loucura(request):
    return HttpResponse("E nessa loucura.......")

def detalhe(request, questao_id):
    # try:
    #     questao = Questao.objects.get(pk=questao_id)
    # except Questao.DoesNotExist:
    #     raise Http404("Questao naum ecxisty")
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'enquete/questao.html', {'questao': questao})


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'enquete/resultado.html', {'questao': questao})


def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        resposta = questao.resposta_set.get(pk=request.POST["resposta"])
    except (KeyError, Resposta.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "enquete/questao.html",
            {
                "questao": questao,
                "error_message": "Esta Resposta naum ecxiste.",
            },
        )
    else:
        resposta.votos += 1
        resposta.save()
        return HttpResponseRedirect(reverse("resultados", args=(questao.id,)))
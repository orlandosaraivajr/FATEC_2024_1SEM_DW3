from django.shortcuts import render
from core.models import FeriadoModel
from datetime import date

def feriado(request):
    hoje = date.today()
    qs = FeriadoModel.objects.filter(mes=hoje.month)
    qs = qs.filter(dia=hoje.day)
    if len(qs) == 1:
        nome_feriado = qs[0].nome
        contexto = {'title':"Meu Feriado", 'feriado':True,
                'nome_feriado':nome_feriado}
    else: 
        contexto = {'title':"Meu Feriado", 'feriado':False}
    return render(request, 'feriado.html', contexto)


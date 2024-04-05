from django.shortcuts import render

def natal(request):
    rua = 'Rua 10'
    contexto = {'natal':False, 'carnaval':False,
                'onde_noel_vai':rua}
    return render(request, 'natal.html', contexto)

def carnaval(request):
    return render(request, 'carnaval.html')
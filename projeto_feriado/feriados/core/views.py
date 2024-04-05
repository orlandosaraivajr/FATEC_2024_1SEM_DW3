from django.shortcuts import render

def natal(request):
    return render(request, 'natal.html')

def carnaval(request):
    return render(request, 'carnaval.html')
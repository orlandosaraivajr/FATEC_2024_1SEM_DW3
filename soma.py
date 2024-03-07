'''
07/03/2024
Desafio: Crie uma função chamada "soma", 
que receba dois parâmetros e retorne a soma dos parâmetros

def soma(parametro1, parametro2):
    return parametro1 + parametro2


Desafio: Crie uma função chamada "soma", 
que receba três parâmetros e retorne a soma dos parâmetros

def soma(parametro1, parametro2, parametro3):
    return parametro1 + parametro2 + parametro3
'''

''' Args e KWargs 

Desafio: Crie uma função chamada "soma", 
que receba parâmetros e retorne a soma dos parâmetros numéricos somente.

'''
def soma(*parametros):
    soma = 0
    for elemento in parametros:
        if type(elemento) == str:
            pass
        else:
            soma = soma + elemento
    return soma


assert soma(1,2,3) == 6
assert soma(1,2) == 3
assert soma(1,2,3,'oi') == 6
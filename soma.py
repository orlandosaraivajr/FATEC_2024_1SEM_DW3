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
        try:
            soma = soma + elemento
        except TypeError:
            # raise TypeError('Soma não suportada')
            pass
    return soma


assert soma(1,2,3) == 6
assert soma(1,2) == 3
assert soma(1, 2, 3, 'oi') == 6
assert soma(1.0, 2.0) == 3.0


'''
KWargs
'''
def teste(**parametros):
    print(parametros)

teste(nome='Orlando')
teste(nome='Orlando',sobrenome='Saraiva')
teste(nome='Orlando',sobrenome='Saraiva',disciplinas=['ED','DW3'])

 
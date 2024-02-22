# Sequencia
print('oi mundo')

print('passo 2')

# Seleção ( IF )
valor1 = 5

if valor1 > 10:
    print("Valor maior que dez")

if valor1 > 2:
    print("Valor maior que dois")

# Iterações com objeto iterável
lista = list(range(1, 10))

for irineu in lista:
    print("Achei: ")
    print(irineu)
    

lista = list(range(1,10))
lista.append('Leite')
lista.append(list(range(1,10)))
lista.append('Café')

# Exibir via print somente os elementos que sejam do tipo string
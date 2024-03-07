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

# Desafio 1
# Exibir via print somente os elementos que sejam do tipo string
print("Encontrando elementos string na lista  \n\n")
for quadradinho in lista:
    if type(quadradinho) == str:
        print(quadradinho)

# Desafio 2
# Dado uma string qualquer, separar as letras com o caracter pipe (|)
# Exemplo:
# Fatec => F | A | T | E | C
 
 
 # 29/02/2024
 # Desafio 3
 # A partir de uma lista, criar uma lista apenas os itens não repetidos.
 
 # Exemplo:
 # Entrada: ["Pão","Leite","Ovo","Farinha" ,"Leite","Ovo"]
 # Saída: ["Pão","Leite","Ovo","Farinha"]
 
lista = ["Pão","Leite","Ovo","Farinha" ,"Leite","Ovo"]

# Sem uso de set:
lista2 = []
for x in lista:
    if x not in lista2:
        lista2.append(x)

# Solução com uso de set:
lista3 = list(set(lista))



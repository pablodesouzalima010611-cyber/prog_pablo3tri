"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    
    nova_lista = []

    for numero in lista:
        if numero >= 0:
            nova_lista.append(numero)

    return nova_lista


print(remove_negativos([1, -2, 3, -4]))
print(remove_negativos([0, -1, 5]))

def inverte(lista):
    nova_lista = []

    for i in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[i])

    return nova_lista


print(inverte([1, 2, 3]))
print(inverte([7]))


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif alvo < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1


print(busca_binaria([1, 3, 5, 7, 9], 5))
print(busca_binaria([1, 3, 5, 7, 9], 4))


def intercala(lista_a, lista_b):
    nova_lista = []

    for i in range(len(lista_a)):
        nova_lista.append(lista_a[i])
        nova_lista.append(lista_b[i])

    return nova_lista


print(intercala([1, 3, 5], [2, 4, 6]))
print(intercala([], []))

def remove_repetidos(lista):
    nova_lista = []

    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)

    return nova_lista


print(remove_repetidos([1, 2, 1, 3, 2]))
print(remove_repetidos([5, 5, 5]))

"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    """Devolve a soma de todos os numeros da lista. Lista vazia devolve 0."""

    if len(lista) == 0:
        return 0

    return lista[0] + soma_lista(lista[1:])


lista = [1, 2, 3, 4, 5]

print(soma_lista(lista))


def conta_pares(lista):
    """Devolve quantos numeros da lista sao pares."""

    if len(lista) == 0:
        return 0

    if lista[0] % 2 == 0:
        return 1 + conta_pares(lista[1:])

    return conta_pares(lista[1:])


lista = [1, 2, 3, 4, 6]

print(conta_pares(lista))


def maior_valor(lista):
    """Devolve o maior numero da lista. A lista nao esta vazia."""

    if len(lista) == 1:
        return lista[0]

    maior = maior_valor(lista[1:])

    if lista[0] > maior:
        return lista[0]

    return maior


print(maior_valor([3, 9, 2, 7]))


def existe(lista, alvo):
    """Devolve True se o alvo esta na lista, False se nao esta."""

    if len(lista) == 0:
        return False

    if lista[0] == alvo:
        return True

    return existe(lista[1:], alvo)


print(existe([4, 8, 15], 8))
print(existe([4, 8, 15], 9))


def busca_linear(lista, alvo, posicao=0):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""

    if len(lista) == 0:
        return -1

    if lista[0] == alvo:
        return posicao

    return busca_linear(lista[1:], alvo, posicao + 1)


print(busca_linear([4, 8, 15], 15))
print(busca_linear([4, 8, 15], 9))


def segundo_maior(lista):
    """Devolve o segundo maior, percorrendo a lista uma unica vez."""

    maior = float('-inf')
    segundo = float('-inf')

    for numero in lista:
        if numero >= maior:
            segundo = maior
            maior = numero
        elif numero > segundo:
            segundo = numero

    return segundo


print(segundo_maior([3, 9, 2, 7]))
print(segundo_maior([5, 5, 1]))
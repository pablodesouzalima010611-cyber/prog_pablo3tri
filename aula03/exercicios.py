"""Aula 03 - Construa e diga o custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

ATENCAO: quase todas as funcoes desta aula devolvem DUAS coisas,
o resultado e a contagem de operacoes:

    return soma, operacoes

Quem devolve so o resultado nao passa nos testes.
"""



def soma_contando(lista):
    soma = 0
    operacoes = 0

    for numero in lista:
        soma += numero
        operacoes += 1

    return soma, operacoes


def busca_linear_contando(lista, alvo):
    comparacoes = 0

    for i in range(len(lista)):
        comparacoes += 1

        if lista[i] == alvo:
            return i, comparacoes

    return -1, comparacoes


def busca_binaria_contando(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista[meio] == alvo:
            return meio, comparacoes

        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes


def tem_repetido_contando(lista):
    comparacoes = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparacoes += 1

            if lista[i] == lista[j]:
                return True, comparacoes

    return False, comparacoes


def quantas_divisoes(n):
    divisoes = 0

    while n > 1:
        n = n // 2
        divisoes += 1

    return divisoes


def mais_frequente_contando(lista):
    if len(lista) == 0:
        return None, 0

    mais_frequente = lista[0]
    maior_contagem = 0
    comparacoes = 0

    for i in range(len(lista)):
        contagem = 0

        for j in range(len(lista)):
            comparacoes += 1

            if lista[i] == lista[j]:
                contagem += 1

        if contagem > maior_contagem:
            maior_contagem = contagem
            mais_frequente = lista[i]

    return mais_frequente, comparacoes

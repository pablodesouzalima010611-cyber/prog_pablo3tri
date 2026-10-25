"""Aula 04 - Por que ordenar?

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Hoje voce NAO escreve algoritmo de ordenacao. Use sorted(lista), que
devolve uma lista nova e ordenada sem mexer na original. Evite lista.sort(),
que altera a lista de quem chamou a funcao.
"""


def custo_binaria(n):
    """PRONTA. Nao mexa."""
    divisoes = 0
    while n > 1:
        n = n // 2
        divisoes = divisoes + 1
    return divisoes + 1


def tem_repetido_ordenando(lista):
    copia = sorted(lista)
    comparacoes = 0

    for i in range(len(copia) - 1):
        comparacoes += 1

        if copia[i] == copia[i + 1]:
            return True, comparacoes

    return False, comparacoes


def mediana(lista):
    if len(lista) == 0:
        return None

    copia = sorted(lista)
    meio = len(copia) // 2

    if len(copia) % 2 == 1:
        return copia[meio]

    return (copia[meio - 1] + copia[meio]) / 2


def buscas_para_compensar(n, custo_ordenar):
    custo_busca = custo_binaria(n)

    diferenca = n - custo_busca

    if diferenca <= 0:
        return -1

    if custo_ordenar < 0:
        return 0

    return custo_ordenar // diferenca + 1


def menor_diferenca(lista):
    if len(lista) < 2:
        return None

    copia = sorted(lista)
    menor = abs(copia[1] - copia[0])

    for i in range(1, len(copia) - 1):
        diferenca = abs(copia[i + 1] - copia[i])

        if diferenca < menor:
            menor = diferenca

        if menor == 0:
            return 0

    return menor
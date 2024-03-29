# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return {
#         (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#     }


cidade =  ['Salvador', 'Ubatuba', 'Belo Horizonte']
sigla = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(cidade, sigla)))
print(list(zip_longest(cidade, sigla, fillvalue='Sem Cidade')))
# reduce - faz a redução de um iterável em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# def func_de_reduce(acumulador, produto):
#     print(acumulador)
#     print(produto)
#     return acumulador + produto['preco']

total = reduce(
    lambda acl, p: acl + p['preco'],
    # func_de_reduce,
    produtos, 
    0
)

print('Total ', total)
# total = 0

# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))
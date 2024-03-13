# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

# from itertools import combinations, permutations, product

# def print_iter(itereitor):
#     print(*list(itereitor), sep='\n')
#     print()

# pessoas = [
#     'João', 'Joana', 'Luiz', 'Letícia',
# ]
# camisetas = [
#     ['preta', 'branca'],
#     ['p', 'm', 'g'],
#     ['masculino', 'feminino', 'unisex'],
#     ['algodão', 'poliester'],
# ]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
# print_iter(product(*camisetas))

# groupby - agrupando valores (itertools)

# from itertools import groupby


# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'A'},
#     {'nome': 'Anderson', 'nota': 'C'},
# ]

# def ordena(aluno):
#     return aluno['nota']

# alunos_agrupados = sorted(alunos, key=ordena)
# grupos = groupby(alunos_agrupados, key=ordena)

# for chave, grupo in grupos:
#     print(chave)
#     for aluno in grupo:
#         print(aluno)
        
# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def amentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)

almentar_dez_porcento = partial(
    amentar_porcentagem,
    porcentagem=1.1
)
    
# novos_produtos = [
#     {**p, 'preco' : almentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]

def muda_preco_de_produto(produto):
    return {**produto, 'preco' : almentar_dez_porcento(produto['preco'])}

novos_produtos = map(
    muda_preco_de_produto,
    produtos
)
# novos_produtos =(x for x in produtos)

print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
print(isinstance(novos_produtos, GeneratorType))


print(
    list(map(
    lambda x: x* 3,
    [1,2,3,4]
    ))
)
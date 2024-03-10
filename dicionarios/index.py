# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# pessoa1 = dict(nome='Caio', sobrenome='Dias')

# pessoa = {
#     'nome' : 'Caio',
#     'sobrenome': 'Dias'
#     }

# pessoa = {
#     'nome': 'Caio',
#     'sobrenome': 'Dias',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }


# print(pessoa['nome'])
# print(pessoa['endereços'])
# # print(pessoa2)
# # print(pessoa)
# print()
# for chaves in pessoa:
#     print(chaves, pessoa[chaves])
    
    
# Manipulando chaves e valores em dicionários

# pessoa = {}

# chaves = 'nome'

# pessoa[chaves] = 'Caio'

# pessoa[chaves] = 'Vini'

# pessoa['sobrenome'] = 'Dias'

# print(pessoa[chaves])
# # del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])

# if pessoa.get('sobrenome') is None:
#     print('NAO EXISTI')
# else:
#     print(pessoa['sobrenome'])

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}
d2 = copy.deepcopy(d1)

d2['c1'] = 100
d2['l1'][1] = 999
for valor in d1['l1']:
    print(valor)
print(d2)

# pessoa = {
#     'nome': 'Caio Dias',
#     'sobrenome': 'Martins',
#     # 'idade': 900,
    
# }

# pessoa.setdefault('idade', 6)
# print(pessoa['idade'])
# print(len(pessoa))

# print(list(pessoa.keys()))
# for chave in pessoa.keys():
#     print(chave)

# print(pessoa.values())
# for valor in pessoa.values():
#     print(valor)

# print(pessoa.items())
# for chaves, valor in pessoa.items():
#     print(chaves, valor)

# print(pessoa['nome'])
# print(pessoa.get('nome', 'nao existe'))

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

# pessoa.update({
#     'nome': 'novo valor',
#     'idade' : 18
# })
# pessoa.update(nome='novo valor', idade=18)


# print(pessoa)
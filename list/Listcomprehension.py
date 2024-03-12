# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = [ ]
for numero in range(10):
    lista.append(numero)
    
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]

# print(lista)

# Mapeamento de dados em list comprehension
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# p(novos_produtos)

# filter da listas

# listaa = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]
# p(novos_produtos)

# List comprehension com mais de um for

listaaa = []
for x in range(3):
    for y in range(3):
        listaaa.append((x,y))
        
listaaa = [ 
        (x,y)
        for x in range(3)
        for y in range (3)
]
        
print(listaaa)

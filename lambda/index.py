# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]

# lista = [4,32, 1,34,5,6,6,21,]

# # lista.sort(reverse=True)
# sorted(lista)
 
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     # print(item)
#     return item['sobrenome']

# def exibir(lista):
#     for items in lista:
#         print(items)
#     print()
    

# l1 = sorted(lista, key=lambda item: item['sobrenome'])
# l2 = sorted(lista, key=lambda items: items['nome'])


# exibir(l1)
# exibir(l2)

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

print(
    executa(
        lambda x,y: x + y,
        2, 3
    )
)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# duplicar = cria_multiplicador(2)
duplicar = executa(
    lambda m: lambda n: m*n,
    2
)
print(duplicar(2))

print(
    executa(
        lambda *args: sum(args),
        1,5,6,4,8,
    )
)
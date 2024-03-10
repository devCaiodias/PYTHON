"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create - Read - Update - Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# lista = [10, 20, 30, 40, 50]
# lista[2] = 300 
# del lista[2]
# lista.append(60) 
# lista.pop(3)
# lista.append(70)
# print(lista)

# listaa = [10, 20, 30, 40]
# listaa.append('Caio Dias')
# nome = listaa.pop()
# listaa.append(123)
# del listaa[-1]
# # listaa.clear()
# listaa.insert(0,1)
# print(listaa, f'Romovido, {nome}')


# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# listas_a = ['Maria', 'Caio']
# listas_b = listas_a.copy()

# listas_a[0] = 'Vinicius'
# print(listas_a)
# print(listas_b)


"""
Lista de listas e seus índices
"""

salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduardo', ],
]

# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
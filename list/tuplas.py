"""
Introdução ao empacotamento e desempacotamento
"""

_,_, nome3, *_ = ['Caio', 'vinicius', 'joao']

print(nome3)

"""
Tipo tupla - Uma lista imutável
"""

nomes = 'Caio', 'Vinicius', 'Jonas'
print(nomes)

'''
enumerate - enumera - iteraveis (indices)
'''

lista = ['Caio', 'vinicius', 'joao']
lista.append(244)

for indice, nome in enumerate(lista):
    print(indice, nome)


# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)
    
# for item in enumerate(lista):
#     for valor in item:
#         print(valor)
    

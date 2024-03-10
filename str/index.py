"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Olha so que, coisa interessante'
lista_frase_crua = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())
print(lista_frase)
    
frase_unidas = ', '.join(lista_frase)
print(frase_unidas)
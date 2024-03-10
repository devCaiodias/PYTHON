texto = 'Python'

nova_texto = ''
for letra in texto:
    nova_texto += f'*{letra}'
    print(letra)
    
print(nova_texto + '*')

print('-'*40)
"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(0,10+1)

for numero in numeros:
    print(numero)
    
    
print('-'*40)
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
tex = 'Caio' #interável
iteratador = iter(tex) #iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break


for i in range(10):
    if i == 2:
        print('i é 2. Pulando...')
        continue
    if i == 8:
        print('i é 8, seu else n será executado!')
        break
        
    for j in (1, 3):
        print(i,j)
else:
    print('For completo com sucesso!')
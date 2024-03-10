def mult(*n1):
    total = 1
    for numero in n1:
        total *= numero
    return total
    
print(mult(1,2,3,4,5))

def parimpar(n):
    numero = n
    if numero % 2 == 0:
        return f'{numero} é Par'
    
    return f'{numero} é Impar'

print(parimpar(2))
print(parimpar(15))
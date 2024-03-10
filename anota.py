"""
    sep = "" # Separador
"""
print(50,41,100, sep='-') # 50-41-100

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite um numero: ')

int_numero1 = int(numero_1)
int_numero2 = int(numero_2)

print(f'A soma dos numeros é {int_numero1 + int_numero2}')


# Not vc inverte a expressões
# not True = False
# not False = True  


'''
 in - está
 not in - não está
'''

print(f'O hexadecimal de 1500 é {1500:08X}')

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    numero_float1 = 0
    numero_float2 = 0
    
    try:
        numero_float1 = float(numero_1)
        numero_float2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números Digitados são inválidos.')
        continue
    
    operador_permitido = '+-/*'
    
    if operador not in operador_permitido:
        print('Operador Invalido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('O Resultado da sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(numero_float1 + numero_float2)
    elif operador == '-':
        print(numero_float1 - numero_float2)
    elif operador == '*':
        print(numero_float1 * numero_float2)
    elif operador == '/':
        print(numero_float1 / numero_float2)
    else:
        print('Isso nunca deveria ter acontecido.')
        
    ###
    
    sair = input('Quar sair? [s]: ').lower().startswith('s')
    
    if sair is True:
        break
    
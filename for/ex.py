import os

palavra_secreta = 'bola'
letras_acertadas = ''

cont = 0
while True:
    letra = input('Digite uma letra: ')
    cont += 1
    
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        
    if letra in palavra_secreta:
        letras_acertadas += letra
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('-'*30)
        print('VC GANHOU PARABENS!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas {cont}')
        break
        
            
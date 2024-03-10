nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if nome == ' ':
        print(f'Meu nome contém espaço')
    else:
        print(f'Meu nome n contém espaço')

    print(f'Seu nome tem {len(nome)} letras')

    print(f'A primeira letra do seu nome é {nome[0:1]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpa, vc deixou campos vazios.')
    
# AULA 49
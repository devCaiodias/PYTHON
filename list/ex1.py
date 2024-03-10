import os

lista_compras = []
while True:
    selecionar = str(input('Selecione uma opção \n' \
                            '[i]nserir  [a]pagar [l]istar: ')).upper()
    if selecionar == 'I':
        os.system('cls')
        lista_compras.append(input('Valor: '))
    elif selecionar == 'A':
        try:
            indice = int(input('Escolha o indice para apagar: '))
            del lista_compras[indice]
        except IndexError:
            print('Não foi possivel apagar este indice')
        except ValueError:
            print('Por Favor! digite so numeros inteiros.')
        
    elif selecionar == 'L':
        os.system('cls')
        if lista_compras == []:
            os.system('cls')
            print('Nada para listar')
        else:
            for indices, compras in enumerate(lista_compras):
                print(indices, compras)
    else:
        print('Por favor, escolha i, a ou l.')
numero_inteiro = input('Digite um numero inteiro: ')

try:
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print('Este numero é PAR!')
    else:
        print('Este numero é IMPAR!')
except ValueError:
    print('Informe so numero inteiro POR FAVOR!')
    
print('-'*40)

hora = input('Imfome seu horario: ')

try:
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom diaa!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('N conheço essa hora.')
except:
    print('Por favor, digite somente numero inteiro')

print('-'*40)

primeiro_nome = input('Digite seu primeiro nome: ')
letras_nome = len(primeiro_nome)

if letras_nome <= 4:
    print('Seu nome é curto')
if letras_nome >= 5 and letras_nome <= 6:
    print('Seu nome é normal')
if letras_nome > 6:
    print('Seu nome é muito grande')
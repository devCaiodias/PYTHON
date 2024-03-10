pergunta = [
    {
        'Pergunta': 'Quantos é 2+2?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for c in range(3):
    print()
    print(f'Pergunta: {pergunta[c]['Pergunta']}')

    print()
    print('Opções:')
    contar = 0
    for valor in pergunta[c]['Opções']:
        print(f'{contar}) {valor}')
        contar += 1
        
    opcao = input('Escolha uma opção: ')
    int_opcao = int(opcao)
    indice_opcao = pergunta[c]['Opções'][int_opcao]

    if indice_opcao == pergunta[c]['Resposta']:
        print('Acertou 🎆')
        acertos += 1
    elif indice_opcao == pergunta[c]['Resposta']:
        print('Acertou 🎆')
        acertos += 1
    elif indice_opcao == pergunta[c]['Resposta']:
        print('Acertou 🎆')
        acertos += 1
    else:
        print('Errou ❌')
        
print()
print(f'Vc acertou {acertos} \nde 3 perguntas.')
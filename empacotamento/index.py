# Empacotamento e desempacotamento de dicionários
a,b = 1, 2
a, b = b,a
# print(a, b)


# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }

# (a1, a2), b = pessoa.items()

# print(a1, a2)
# print(b)

# for chaves,valor in pessoa.items():
#     print(chaves, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade':15,
    'altura': 1.72
}
pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostrar_argumento_nomeado(*args, **kwargs):
    print('N NOMEADOS: ', args)
    for chaves, valor in kwargs.items():
        print(chaves, valor)
        
    
# mostrar_argumento_nomeado(nome='Caio', idade=15)

mostrar_argumento_nomeado(**pessoa_completa)

configuracao = {
    'args1' : 1,
    'args2' : 2,
    'args3' : 3,
    'args4' : 4
}

mostrar_argumento_nomeado(**configuracao)
"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print():
#     print('Variavel')

# Print()

# def imprimir(a,b,c):
#     print(a,b,c)
    
# imprimir(5,9,4)

# def saudacao(nome = 'Sem nome'):
#     print(f'Olá {nome}')
    
# saudacao('Caio')
# saudacao()

"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x,y):
#     print(f'{x=}  {y=} | x + y = {x + y}')
    
# soma(x=10, y=4)


"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

# def soma(x,y,z=0):
#     if z:
#         print(f'{x=} {y=} {z=}',x + y + z)
#     else:
#         print(f'{x=} {y=}',x + y )
        
# soma(15,13)
# soma(14,5,0)

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# x =1 

# def escopo():
#     # global x
#     x = 10
#     def outra_func():
#         y = 2
#         print(x,y)
#     outra_func()
#     print(x)

# print(x)
# escopo()
# print(x)

"""
Retorno de valores das funções (return)
"""

# def soma(a,b):
#     return a + b

# soma1 = soma(2,5)
# soma2 = soma(4,7)

# print(soma1 + soma2)

"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# def soma(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#         print(total)
#     return total
        
# numeros = 1,2,3,5
# soma1 = soma(*numeros)

# print(soma1)

"""
Higher Order Functions
Funções de primeira classe
"""

# def saudacao(msg, nome):
#     return f'{msg}, {nome}!'

# def executar(funcao, *args):
#     return funcao(*args)

# print(executar(saudacao, 'Bom dia', 'Caio'))
# print(executar(saudacao, 'Bom noite', 'Vini'))

"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia' )
falar_boa_noite = criar_saudacao('Boa noite')
# print(falar_bom_dia('Caio'))
# print(falar_boa_noite('Caio'))

for nome in ['Maria', 'Caio', 'Vini']:
    print(falar_bom_dia(nome))
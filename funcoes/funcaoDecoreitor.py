# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

# def criar_fuc(func):
#     def interna(*args, **kwargs):
#         print('Vou te decorar!')
#         for arg in args:
#             is_string(arg)
#         resultado = func(*args, **kwargs)
#         print(f'O seu resoltado foi {resultado}')
#         print('Ok, agora vc foi decorada')
#         return resultado
#     return interna

# @criar_fuc
# def inverte_string(string):
#     return string[::-1]

# def is_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string')


# inverte = inverte_string('125')
# print(inverte)


# Decoradores com parâmetros

# def fabrica_de_decoradores(a = None, b = None, c = None):
#     def fabrica_de_func(func):
#         print('Decoradora 1')
        
#         def aninhada(*args, **kwargs):
#             print(f'Parametros do decorador, {a,b,c}')
#             print('Aninhada')
#             res = func(*args, **kwargs)
#             return res
#         return aninhada
#     return fabrica_de_func

# @fabrica_de_decoradores(1,5,3)
# def soma(x,y):
#     return x + y

# decoradora = fabrica_de_decoradores()
# multiplicacao = decoradora(lambda x, y: x * y)

# dez_mais_cinco = soma(10,5)
# mutiplica = multiplicacao(5,10)
# print(dez_mais_cinco)
# print(mutiplica)

# Ordem dos decoradores

def parametro_decorado(nome):
    def decorador(func):
        print(f'Decorador: ', nome)
        
        def sua_nova_func(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_func
    return decorador

@parametro_decorado(nome='quarto')
@parametro_decorado(nome='terceiro')
@parametro_decorado(nome='sengundo')
@parametro_decorado(nome='Primeiro')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(5,5)
print(dez_mais_cinco)
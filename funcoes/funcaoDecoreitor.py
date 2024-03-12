# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
def criar_fuc(func):
    def interna(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resoltado foi {resultado}')
        print('Ok, agora vc foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_fuc(inverte_string)
inverte = inverte_string_checando_parametro('125')
print(inverte)
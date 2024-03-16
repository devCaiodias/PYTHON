# Problema dos parâmetros mutáveis em funções Python

def add_cliente_lista(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente_1 = add_cliente_lista('Caio')
add_cliente_lista('Vinicius', cliente_1)
add_cliente_lista('Fernado', cliente_1)
cliente_1.append('Kait')

cliente_2 = add_cliente_lista('joao')
add_cliente_lista('debora', cliente_2)

cliente_3 = add_cliente_lista('gon')
add_cliente_lista('yuta', cliente_3)

print(cliente_1)
print(cliente_2)
print(cliente_3)
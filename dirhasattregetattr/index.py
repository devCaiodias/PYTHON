# dir, hasactr e getattr em python

string = 'Caio'
metado = 'lower'
# print(dir(string))

if hasattr(string, metado):
    print(f'Existie {metado}')
    print(getattr(string, metado)())
else:
    print(f'Existe nem um {metado}')
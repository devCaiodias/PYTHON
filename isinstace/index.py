# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item)
        print('-------------------')
        
    elif isinstance(item, str):
        print('STR')
        print(item.upper())
        print('-------------------')
        
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
        print('-------------------')
    else:
        print('OUTROS')
        print(item)
        
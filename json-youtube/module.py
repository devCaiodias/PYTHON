import json
import os

pessoa = [
    {
        "nome" : 'Caio',
        "sobrenome" : 'dias',
        "idade" : 18,
        "ativo" : False,
        "nota" : ['A', 'A+'],
        "telefone": {
            "residencial": "00 0000-0000",
            "celular" : "00 0000-0000",
            }
    
    },
    {
        "nome" : 'vini',
        "sobrenome" : 'mendz',
        "idade" : 19,
        "ativo" : True,
        "nota" : ['B', 'B+'],
        "telefone": {
            "residencial": "00 1111-0000",
            "celular" : "00 1111-0000",
            }
    },  
]

# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, "arquivo-python.json")

# with open(SAVE_TO, 'w') as file:
#     json.dump(pessoa, file, indent=2)
    
print(json.dumps(pessoa, indent=2))

    
    
# json_string = '''
# [{"nome": "Caio", "sobrenome": "dias", "idade": 18, "ativo": false, "nota": ["A", "A+"], "telefone": {"residencial": "00 0000-0000", "celular": "00 0000-0000"}}, {"nome": "vini", "sobrenome": "mendz", "idade": 19, "ativo": true, "nota": ["B", "B+"], "telefone": {"residencial": "00 1111-0000", "celular": "00 1111-0000"}}]
# '''

# pessoa = json.loads(json_string)

# for p in pessoa:
#     print(p)
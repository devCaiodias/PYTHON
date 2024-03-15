import json
import os

pessoa = {
    'nome': 'Caio',
    'sobrenome': 'Dias',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

caminho_arquivo = 'C:\\Users\\caiod\\pyhard\\json-udem\\'
caminho_arquivo += 'aquivo-python.json'

with open(caminho_arquivo, 'w', encoding='utf8') as file:
    json.dump(pessoa, 
              file, 
              indent=2, 
              ensure_ascii=False
              )

with open(caminho_arquivo, 'r', encoding='utf8') as file:
    pessoa = json.load(file)
    print(pessoa)
    print(pessoa['nome'])
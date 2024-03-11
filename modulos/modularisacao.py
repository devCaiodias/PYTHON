# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# try:
#     import sys
#     sys.path.append('/Users/caiod')
# except ModuleNotFoundError:
#     ...
# import modulo_python

import modulo_m
from modulo_m import soma, variavel_modulo

print(f'Esse modulo se chama {__name__}')
# print(variavel_modulo)
print(modulo_m.variavel_modulo)

# print(soma(2,1))
print(modulo_m.soma(2,1))

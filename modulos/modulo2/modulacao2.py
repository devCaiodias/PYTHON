import importlib

import modulo_m2

print(modulo_m2.variavel)

for i in range(10):
    importlib.reload(modulo_m2)
    
    
print('Fim')